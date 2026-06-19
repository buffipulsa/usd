# My USD Learning Workspace

This repository is my workspace for learning Pixar USD with Python. I use it to
write small, focused examples that I can run, inspect, and build on as I learn
more about stages, layers, prims, schemas, and scene composition.

The project uses `uv` for the Python environment, `usd-core` for the USD Python
bindings, and a local `src` package for my scripts and shared tools.

## Getting Started

```powershell
uv sync
uv run python src/stage/create_stage.py
```

My scripts write generated USD files to `out/`. Git keeps the directory through
`out/.gitkeep`, while the generated `.usd`, `.usda`, and `.usdc` files remain
ignored.

## Project Layout

```text
src/
  prim/
    create_prim_hierarchy.py
    defining_a_prim.py
    defining_sphere_prim.py
    does_prim_exist.py
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

- `src/stage/` contains my examples for creating, opening, saving, and composing
  USD stages and layers.
- `src/prim/` contains my examples for defining, organizing, and finding prims.
- `src/tools/path_tools.py` contains path helpers shared by my scripts.
- `typings/pxr/` contains local stubs I maintain for better USD autocomplete in
  VS Code and Pylance.
- `.vscode/settings.json` configures VS Code for my `uv` environment and hides
  Python cache folders from Explorer.

## Running My Examples

I run scripts from the repository root so imports and output paths stay
consistent.

### Stage Examples

```powershell
uv run python src/stage/create_stage.py
uv run python src/stage/create_stage_in_memory.py
uv run python src/stage/open_and_save_stage.py
uv run python src/stage/stage_root_layer.py
```

### Prim Examples

```powershell
uv run python src/prim/defining_a_prim.py
uv run python src/prim/defining_sphere_prim.py
uv run python src/prim/create_prim_hierarchy.py
uv run python src/prim/does_prim_exist.py
```

## What I Am Exploring

- Creating file-backed and in-memory stages.
- Opening, editing, saving, and exporting stages.
- Working with root layers and relative sublayer paths.
- Defining typed and untyped prims.
- Using `UsdGeom` schemas to author geometry prims and attributes.
- Building prim hierarchies with `Sdf.Path`.
- Looking up prims and their children.

## Imports

I import shared helpers through the `src` package:

```python
import src.tools.path_tools as path_tools
```

The editable `uv` environment installs that package using the Hatchling
configuration in `pyproject.toml`:

```toml
[tool.hatch.build.targets.wheel]
packages = ["src"]
```

## Type Checking And IntelliSense

I run Pyright across my source code with:

```powershell
uv run pyright src
```

The official `usd-core` wheel does not provide complete Python type stubs. I
keep generated and hand-edited stubs in `typings/pxr/` for the USD APIs used by
my examples.

When autocomplete does not refresh after a stub change, I use one of these VS
Code commands:

```text
Python: Restart Language Server
Developer: Reload Window
```

## Notes I Want To Remember

- A `Usd.Stage` is the editable scene graph and owns a root layer.
- A `Usd.Prim` is a scene graph node at a path such as `/World`.
- An `Sdf.Layer` represents a USD layer, including `.usda` and `.usdc` files.
- Sublayer paths are authored relative to the layer that contains them.
- USD asset paths should use forward slashes, including on Windows.
