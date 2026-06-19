"""Define untyped and typed prims on a USD stage.

This module creates ``out/prims.usda``, authors an untyped ``/hello`` prim and
a ``Sphere``-typed ``/world`` prim, then saves and prints the stage.

Notes
-----
``Usd.Stage.DefinePrim`` creates any missing ancestors needed for the supplied
prim path. Omitting ``typeName`` authors a prim without a concrete schema type.
"""

from pxr import Usd

import src.tools.path_tools as path_tools

root_path = path_tools.find_repo_root()

file_path = root_path / "out" / "prims.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(str(file_path))

stage.DefinePrim("/hello")

stage.DefinePrim("/world", "Sphere")

stage.Save()

print(stage.ExportToString(addSourceFileComment=False))
