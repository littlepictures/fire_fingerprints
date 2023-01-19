from pathlib import Path
import os
import sys

_UTILS_REPO = "pytrevalabs"
_UTILS_MODULE = "cliplib"

_UTILS_PATH = Path(_UTILS_REPO, _UTILS_MODULE)


def _get_workspace_path():
    """Determine workspace path and expand sys.path so we can import 
    package "cliplib".
    
    Workpace path is made accessible via global variable ws_path".
    """
    ws_path = Path(os.getcwd()).absolute()
    while ws_path and ws_path != Path("/"):
        if (ws_path / _UTILS_PATH).is_dir():
            return ws_path
        ws_path = ws_path.parent
    raise RuntimeError(f"Cannot find Treva Labs utilities {_UTILS_PATH}")

ws_path = _get_workspace_path()
if ws_path not in sys.path:
    sys.path = [str(ws_path / _UTILS_REPO)] + sys.path

import cliplib
