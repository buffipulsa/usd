"""Create a new USD stage on disk.

This module creates ``out/first_stage.usda`` relative to the repository root and
prints the newly authored stage as USDA text.

Notes
-----
The script uses ``Usd.Stage.CreateNew`` to create a file-backed stage. The stage
is not explicitly saved here; printing ``ExportToString`` shows the authored
layer contents currently held by the stage.
"""

from pxr import Usd

import src.tools.path_tools as path_tools

root_path = path_tools.find_repo_root()

file_path = root_path / "out" / "first_stage.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(str(file_path))
print(stage.ExportToString(addSourceFileComment=False))
