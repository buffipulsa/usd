"""Create an in-memory USD stage and export it to disk.

This module demonstrates ``Usd.Stage.CreateInMemory`` by authoring a simple
``/World`` prim, printing the stage contents, and exporting the result to
``out/in_memory_stage.usda``.

Notes
-----
In-memory stages are useful for experiments because they do not require an
output file until ``Export`` is called.
"""

from pxr import Usd

import src.tools.path_tools as path_tools

stage: Usd.Stage = Usd.Stage.CreateInMemory()

stage.DefinePrim("/World", "Xform")

print(
    "In-memory stage: ",
    stage.ExportToString(addSourceFileComment=False)
)

root_path = path_tools.find_repo_root()

file_path = root_path / "out" / "in_memory_stage.usda"

stage.Export(str(file_path))
