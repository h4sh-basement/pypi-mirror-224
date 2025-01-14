# RepRepBuild is the build tool for Reproducible Reporting.
# Copyright (C) 2023 Toon Verstraelen
#
# This file is part of RepRepBuild.
#
# RepRepBuild is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# RepRepBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --
"""Main driver for building a manuscript or publication from its sources.

When the package installed, the script rr is the entry point to the main
function below. It ignores any arguments. In the directory where it is
executed, the relative path latex_main/main.tex must exist. It will create a new
file build.ninja (or overwrite an existing one) and then run ninja.

The details of the build process cannot be influenced by command-line arguments.
This is by design, to have only one (reproducible) way to build the publication
from the source, for which all the settings and details are stored in files.
"""

import os
import re
import subprocess
import sys
from glob import glob

from ninja.ninja_syntax import Writer

from .utils import format_case_args, import_python_path

__all__ = ("main",)


LATEXDIFF_CONTEXT2CMD = ",".join(
    [
        "abstract",
        "supplementary",
        "dataavailability",
        "funding",
        "authorcontributions",
        "conflictsofinterest",
        "abbreviations",
    ]
)


DEFAULT_RULES = {
    "latexdep": {"command": "rr-latexdep $in", "depfile": "$in.d"},
    "bibtex": {"command": "rr-bibtex $in", "depfile": "$in.d"},
    "latex": {"command": "rr-latex $in"},
    "copy": {"command": "cp $in $out"},
    "latexdiff": {"command": f"latexdiff --append-context2cmd={LATEXDIFF_CONTEXT2CMD} $in > $out"},
    "latexflat": {"command": "rr-latexflat $in > $out"},
    "reprozip": {"command": "rr-zip $out $in"},
    "reproarticlezip": {"command": "rr-article-zip $out $in"},
    "svgtopdf": {
        "command": "inkscape $in -T --export-filename=$out --export-type=pdf; rr-normalize-pdf $out"
    },
    "pythonscript": {
        "command": "rr-python-script $in -- $argstr > $out",
        "depfile": "$out_prefix.d",
    },
}


def latex_pattern(path):
    """Make ninja build commands to compile latex with pdflatex."""
    result = re.match(r"latex-(?P<prefix>[a-z0-9-]+)/(?P=prefix).tex$", path)
    if not result:
        return
    prefix = result.group("prefix")
    workdir = f"latex-{prefix}"

    def fixpath(fn_local):
        return os.path.normpath(os.path.join(workdir, fn_local))

    yield {
        "outputs": fixpath(f"{prefix}.tex.dd"),
        "implicit_outputs": [
            fixpath(f"{prefix}.aux"),
            fixpath(f"{prefix}.first.aux"),
            fixpath(f"{prefix}.fls"),
            fixpath(f"{prefix}.log"),
        ],
        "rule": "latexdep",
        "inputs": fixpath(f"{prefix}.tex"),
    }
    yield {
        "outputs": fixpath(f"{prefix}.bbl"),
        "implicit_outputs": fixpath(f"{prefix}.blg"),
        "rule": "bibtex",
        "inputs": fixpath(f"{prefix}.first.aux"),
    }
    yield {
        "outputs": fixpath(f"{prefix}.pdf"),
        "rule": "latex",
        "inputs": fixpath(f"{prefix}.tex"),
        "order_only": fixpath(f"{prefix}.tex.dd"),
        "dyndep": fixpath(f"{prefix}.tex.dd"),
    }
    yield {
        "outputs": os.path.join("uploads", f"{prefix}.pdf"),
        "rule": "copy",
        "inputs": fixpath(f"{prefix}.pdf"),
        "default": True,
    }
    if prefix in ["article", "supp"]:
        yield {
            "outputs": os.path.join("uploads", f"{prefix}.zip"),
            "implicit_outputs": fixpath(f"{prefix}.sha256"),
            "rule": "reproarticlezip",
            "inputs": f"latex-{prefix}/{prefix}.pdf",
            "default": True,
        }
    fn_old_tex = fixpath(f"old/{prefix}.tex")
    if os.path.isfile(fn_old_tex):
        yield {
            "outputs": fixpath(f"{prefix}-diff.bbl"),
            "rule": "latexdiff",
            "inputs": [fixpath(f"old/{prefix}.bbl"), fixpath(f"{prefix}.bbl")],
        }
        yield {
            "outputs": fixpath(f"{prefix}-flat.tex"),
            "rule": "latexflat",
            "implicit": fixpath(f"{prefix}.pdf"),
            "inputs": fixpath(f"{prefix}.tex"),
        }
        yield {
            "outputs": fixpath(f"old/{prefix}-flat.tex"),
            "rule": "latexflat",
            "inputs": fixpath(f"old/{prefix}.tex"),
        }
        yield {
            "outputs": fixpath(f"{prefix}-diff.tex"),
            "rule": "latexdiff",
            "order_only": fixpath(f"{prefix}-diff.bbl"),
            "inputs": [fixpath(f"old/{prefix}-flat.tex"), fixpath(f"{prefix}-flat.tex")],
        }
        yield {
            "outputs": fixpath(f"{prefix}-diff.tex.dd"),
            "implicit_outputs": [
                fixpath(f"{prefix}-diff.aux"),
                fixpath(f"{prefix}-diff.first.aux"),
                fixpath(f"{prefix}-diff.fls"),
                fixpath(f"{prefix}-diff.log"),
            ],
            "rule": "latexdep",
            "inputs": fixpath(f"{prefix}-diff.tex"),
        }
        yield {
            "outputs": fixpath(f"{prefix}-diff.pdf"),
            "rule": "latex",
            "inputs": fixpath(f"{prefix}-diff.tex"),
            "order_only": fixpath(f"{prefix}-diff.tex.dd"),
            "dyndep": fixpath(f"{prefix}-diff.tex.dd"),
        }
        yield {
            "outputs": os.path.join("uploads", f"{prefix}-diff.pdf"),
            "rule": "copy",
            "inputs": fixpath(f"{prefix}-diff.pdf"),
            "default": True,
        }


def dataset_pattern(path):
    """Make ninja build commands to ZIP datasets."""
    result = re.match(r"(?P<name>dataset[a-z0-9-]*)/MANIFEST.sha256$", path)
    if not result:
        return
    name = result.group("name")
    yield {
        "outputs": f"uploads/{name}.zip",
        "rule": "reprozip",
        "inputs": f"{name}/MANIFEST.sha256",
        "pool": "console",
        "default": True,
    }


def svg_pattern(path):
    """Make ninja build commands to convert SVG to PDF files."""
    result = re.match(r"(?P<name>[a-z][a-z0-9-]*/[a-zA-Z0-9/_-]+).svg$", path)
    if not result:
        return
    name = result.group("name")
    yield {
        "outputs": f"{name}.pdf",
        "rule": "svgtopdf",
        "inputs": f"{name}.svg",
        "default": True,
    }


def python_script_pattern(path):
    """Make ninja build commands for python scripts."""
    # for any valid python file
    if not re.match(r"(?P<name>results(-[a-z0-9_-]*)?/[a-zA-Z0-9/_-]*).py$", path):
        return

    # Call reprepbuild_info as if the script is running in its own directory.
    orig_workdir = os.getcwd()
    workdir, fn_py = os.path.split(path)
    script_prefix = fn_py[:-3]
    try:
        # Load the script in its own directory
        os.chdir(workdir)
        pythonscript = import_python_path(fn_py)

        # Ignore script if the import failed.
        if pythonscript is None:
            yield "Skipped: import failed"
            return
        # Get the relevant functions
        reprepbuild_info = getattr(pythonscript, "reprepbuild_info", None)
        if reprepbuild_info is None:
            yield "Skipped: missing reprepbuild_info"
            return
        reprepbuild_cases = getattr(pythonscript, "reprepbuild_cases", None)
        if reprepbuild_cases is None:
            build_cases = [[]]
        else:
            build_cases = reprepbuild_cases()
        case_fmt = getattr(pythonscript, "REPREPBUILD_CASE_FMT", None)

        def fixpath(fn_local):
            return os.path.normpath(os.path.join(workdir, fn_local))

        # Loop over all cases to make build records
        for script_args in build_cases:
            build_info = reprepbuild_info(*script_args)
            argstr = format_case_args(script_args, script_prefix, case_fmt)
            out_prefix = fixpath(script_prefix if argstr == "" else argstr)
            fn_log = f"{out_prefix}.log"
            implicit_inputs = [fixpath(ipath) for ipath in build_info.get("inputs", [])]
            implicit_outputs = [fixpath(opath) for opath in build_info.get("outputs", [])]
            yield {
                "inputs": path,
                "implicit": implicit_inputs,
                "rule": "pythonscript",
                "implicit_outputs": implicit_outputs,
                "outputs": fn_log,
                "variables": {
                    "argstr": argstr,
                    "out_prefix": out_prefix,
                },
                "default": True,
            }
    finally:
        os.chdir(orig_workdir)


def find_missing_dataset(build):
    """Return a list of missing input files from the datasets."""
    missing = []
    for key in "inputs", "implicit":
        inputs = build.get(key, [])
        if isinstance(inputs, str):
            inputs = [inputs]
        for path in inputs:
            if path.startswith("dataset") and not os.path.exists(path):
                missing.append(path)
    return missing


def check_tex_outputs(outputs: list[str] | str | None):
    """Raise an error when something produces a file with extension ``.tex``

    When this is the case, the function raises an error recommends ``.itex`` instead for
    autogenerated LaTeX sources.
    """
    if outputs is None:
        return
    if isinstance(outputs, str):
        outputs = [outputs]
    for path_out in outputs:
        if path_out.endswith(".tex") and not (
            path_out.endswith("-diff.tex") or path_out.endswith("-flat.tex")
        ):
            raise ValueError(
                "Programatically generated LaTeX files cannot end with '.tex' because this "
                "would not allow for a distinction with static tex files in the build process. "
                r"For example, use '.itex' instead and update the \input commands accordingly."
            )


def write_ninja(patterns, rules):
    """Search through the source for patterns that can be translated into ninja build commands."""
    # Loop over all files and create rules and builds for them
    with open("build.ninja", "w") as f:
        writer = Writer(f, 100)

        # Write all rules, even if some are not used.
        writer.comment("All rules")
        for name, rule in rules.items():
            writer.rule(name=name, **rule)
        writer.newline()

        # Write all build lines and comments
        for path in glob("*/*"):
            builds = []
            for pattern in patterns:
                builds.extend(pattern(path))
            if len(builds) > 0:
                writer.comment(path)
                for build in builds:
                    if isinstance(build, str):
                        writer.comment(build)
                    else:
                        missing = find_missing_dataset(build)
                        if len(missing) > 0:
                            writer.comment("Skipping due to missing dataset files:")
                            for ds_path in missing:
                                writer.comment(ds_path)
                        else:
                            default = build.pop("default", False)
                            check_tex_outputs(build.get("outputs", None))
                            check_tex_outputs(build.get("implicit_outputs", None))
                            writer.build(**build)
                            if default:
                                writer.default(build["outputs"])
                writer.newline()


DEFAULT_PATTERNS = [
    latex_pattern,
    dataset_pattern,
    svg_pattern,
    python_script_pattern,
]


def parse_args():
    """Parse command-line arguments."""
    args = sys.argv[1:]
    if any(arg in ["-?", "-h", "--help"] for arg in args):
        print("All command-line arguments are passed on to the ninja subprocess.")
        print("Run `ninja -h` for details.")
        sys.exit(2)
    return args


def sanity_check():
    """Is there any latex-* folder with tex files?"""
    if len(glob("latex-*/*.tex")) == 0:
        print("Wrong directory? No file matching latex-*/*.tex")
        sys.exit(1)


def main():
    """Main program."""
    sanity_check()
    args = parse_args()
    write_ninja(DEFAULT_PATTERNS, DEFAULT_RULES)
    subprocess.run(["ninja", *args])


if __name__ == "__main__":
    main()
