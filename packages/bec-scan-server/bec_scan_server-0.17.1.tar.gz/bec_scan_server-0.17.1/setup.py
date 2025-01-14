import os
import pathlib
import subprocess
import sys

from setuptools import setup

current_path = pathlib.Path(__file__).parent.resolve()

bec_lib = f"{current_path}/../bec_lib/"

__version__ = "0.17.1"


def run_install(setup_args: dict, bec_deps: list, editable=False):
    """
    Run the setup function with the given arguments.

    Args:
        setup_args (dict): Arguments for the setup function.
        bec_deps (list): List of tuples with the dependencies.
        editable (bool, optional): If True, the dependencies are installed in editable mode. Defaults to False.
    """
    if editable:
        # check if "[dev]" was requested
        if "dev" in os.environ.get("EXTRAS_REQUIRE", ""):
            suffix = "[dev]"
        else:
            suffix = ""
        setup(**setup_args)
        deps = [dep[2] for dep in bec_deps]
        for dep in deps:
            subprocess.run(f"pip install -e {dep}{suffix}", shell=True, check=True)
        return

    install_deps = [dep[0] for dep in bec_deps]
    setup_args["install_requires"].extend(install_deps)
    print(setup_args)
    setup(**setup_args)


if __name__ == "__main__":
    setup_args = {
        "entry_points": {"console_scripts": ["bec-scan-server = scan_server:main"]},
        "install_requires": ["numpy", "msgpack", "pyyaml", "cytoolz", "rich"],
        "version": __version__,
        "extras_require": {"dev": ["pytest", "pytest-random-order", "coverage", "black", "pylint"]},
    }
    bec_deps = [
        ("bec_lib", "bec_lib", bec_lib),
    ]
    is_local = os.path.dirname(os.path.abspath(__file__)).split("/")[-1] == "scan_server"
    is_build = "bdist_wheel" in sys.argv

    editable = is_local and not is_build
    run_install(setup_args, bec_deps, editable=editable)
