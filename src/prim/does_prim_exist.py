"""Look up a prim and test whether it has a named child.

This module opens ``out/prim_hierarchy.usda``, retrieves ``/Geometry``, and
checks whether that prim has a direct child named ``Box``.

Notes
-----
``Usd.Prim.GetChild`` searches only immediate children. In the hierarchy made
by ``create_prim_hierarchy.py``, ``Box`` belongs to ``/Geometry/GroupTransform``
rather than directly to ``/Geometry``.
"""

from pxr import Usd

import src.tools.path_tools as path_tools

root_path = path_tools.find_repo_root()
file_path = root_path / "out" / "prim_hierarchy.usda"

stage: Usd.Stage = Usd.Stage.Open(str(file_path))

prim: Usd.Prim = stage.GetPrimAtPath("/Geometry")

if child_prim := prim.GetChild("Box"):
    print("Child prim exists")
else:
    print("Child prim DOES NOT exist")

print(stage.ExportToString(addSourceFileComment=False))
