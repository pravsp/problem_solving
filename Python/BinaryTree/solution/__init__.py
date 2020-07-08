import os
import sys


def AddSysPath(new_path):
    """ AddSysPath(new_path): adds a directory to python's sys.path

    Does not add the directory if it doesnt exists or if its already on
    sys.path. Return 1 if OK, -1 if new_path doesnt exists, 0 if it was already
    on sys.path
    """
    # Avoid adding non existent of paths
    if not os.path.exists(new_path):
        return -1

    for x in sys.path:
        x = os.path.abspath(x)
        if new_path in (x, x + os.sep):
            return 0
    sys.path.append(new_path)
    return 1

MODULE_PATH = os.path.dirname(__file__)
REPO_PATH = os.path.dirname(MODULE_PATH) 
AddSysPath(REPO_PATH)
