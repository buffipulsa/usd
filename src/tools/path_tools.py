
from pathlib import Path


def find_repo_root(start_path: Path | None = None) -> Path:
    
    path = (start_path or Path(__file__)).resolve()
    
    for parent in [path, *path.parents]:
        if (parent / 'pyproject.toml').exists():
            return parent
        
    raise RuntimeError("Could not find repo root")