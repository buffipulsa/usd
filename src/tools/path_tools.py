"""Path utilities for the USD learning project."""

from pathlib import Path


def find_repo_root(start_path: Path | None = None) -> Path:
    """Find the repository root by walking upward to ``pyproject.toml``.

    Parameters
    ----------
    start_path : pathlib.Path, optional
        Path to start searching from. When omitted, the search starts from this
        module file.

    Returns
    -------
    pathlib.Path
        Absolute path to the first parent directory containing
        ``pyproject.toml``.

    Raises
    ------
    RuntimeError
        If no parent directory contains ``pyproject.toml``.

    Notes
    -----
    This helper avoids hard-coding assumptions about how deeply a script is
    nested inside the repository.
    """
    path = (start_path or Path(__file__)).resolve()

    for parent in [path, *path.parents]:
        if (parent / "pyproject.toml").exists():
            return parent

    raise RuntimeError("Could not find repo root")
