# USD Learning Environment

Small, runnable exercises for learning Pixar USD with Python. The project uses
`uv` and the `usd-core` Python package, so every command below should run inside
the repo without a separate USD install.

## Quick Start

```powershell
uv sync
uv run python examples/01_create_stage.py
```

That command writes a simple stage to `out/hello_scene.usda`.

## Exercises

Run these in order:

```powershell
uv run python examples/01_create_stage.py
uv run python examples/02_layers_and_references.py
uv run python tools/inspect_stage.py out/hello_scene.usda
uv run python tools/inspect_stage.py out/shot.usda
```

The generated `.usda` files are plain text. Open them after each exercise and
compare the file contents with the Python script that created them.

## Project Layout

- `examples/01_create_stage.py` creates a simple animated scene.
- `examples/02_layers_and_references.py` builds an asset file, a shot file, and
  references the asset into the shot.
- `tools/inspect_stage.py` prints prims, types, authored transforms, and basic
  metadata for any USD stage.
- `out/` is for generated learning files and is ignored by git.

## Useful Concepts To Watch

- A `Usd.Stage` is the editable scene graph.
- A `Usd.Prim` is a scene graph node.
- A schema such as `UsdGeom.Xform` or `UsdGeom.Cube` gives typed behavior to a
  prim.
- Attributes store typed values, including time-sampled animation.
- Layers are USD files. Composition arcs such as references combine layers into
  larger scenes.
