# USD Learning Environment

A small Python workspace for learning Pixar USD by writing scripts yourself. The
project uses `uv`, `usd-core`, and a local `src` package layout so examples can
share helper code while staying easy to run and inspect.

## Quick Start

```powershell
uv sync
uv run python src/stage/create_stage.py
```

Generated USD files are written to `out/`. The folder is kept in git with
`out/.gitkeep`, but generated `.usd`, `.usda`, and `.usdc` files are ignored.

## Project Layout

```text
src/
  stage/
    create_stage.py
    create_stage_in_memory.py
    open_and_save_stage.py
    stage_root_layer.py
  tools/
    path_tools.py
typings/
  pxr/
out/
  .gitkeep
```

- `src/stage/` contains small USD learning scripts.
- `src/tools/path_tools.py` contains shared path helpers.
- `typings/pxr/` contains local stubs for better VS Code/Pylance autocomplete.
- `.vscode/settings.json` points VS Code at the `uv` environment and hides Python
  cache folders from Explorer.

## Running The Scripts

Run the stage examples from the repository root:

```powershell
uv run python src/stage/create_stage.py
uv run python src/stage/create_stage_in_memory.py
uv run python src/stage/open_and_save_stage.py
uv run python src/stage/stage_root_layer.py
```

The scripts currently cover:

- Creating a file-backed stage with `Usd.Stage.CreateNew`.
- Creating an in-memory stage with `Usd.Stage.CreateInMemory`.
- Opening and saving an existing stage with `Usd.Stage.Open` and `Save`.
- Creating a root layer and adding a relative sublayer path.

## Imports

This project intentionally imports helper modules through the `src` package:

```python
import src.tools.path_tools as path_tools
```

The package is installed through the editable `uv` environment using the Hatchling
configuration in `pyproject.toml`:

```toml
[tool.hatch.build.targets.wheel]
packages = ["src"]
```

## Type Checking And IntelliSense

Run Pyright with:

```powershell
uv run pyright src
```

The official `usd-core` wheel does not provide complete Python type stubs. The
`typings/pxr/` directory contains local generated and hand-edited stubs so VS
Code can provide better autocomplete for the USD APIs used in this project.

If autocomplete does not refresh after stub changes, run one of these VS Code
commands:

```text
Python: Restart Language Server
Developer: Reload Window
```

## Useful Concepts To Watch

- A `Usd.Stage` is the editable scene graph and owns a root layer.
- A `Usd.Prim` is a scene graph node such as `/World`.
- `Sdf.Layer` represents a USD layer file such as `.usda` or `.usdc`.
- Sublayer paths are authored relative to the layer that contains them.
- USD asset paths should use forward slashes, even on Windows.
