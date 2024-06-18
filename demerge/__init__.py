__all__ = ["analysis", "merge"]
__version__ = "2.13.0"


# submodules
from . import analysis, merge


def cli() -> None:
    """Run run.sh (works on Linux-like systems)."""
    from pathlib import Path
    from subprocess import run
    from sys import argv

    cmd = Path(__file__).parent / "cli.sh"
    run([cmd, *argv[1:]])
