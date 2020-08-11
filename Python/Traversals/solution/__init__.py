"""Doc.
Additional code add to __init__ files which have scripts which you
want to run as standalone scripts
"""

from builtins import range
import os
import site


def find_base_repo_path():
    """Get the root of current repo.
    :return: path
    """
    path_list = os.path.realpath(__file__).split("/")
    for i in range(len(path_list) - 1, -1, -1):
        base_path = "/".join(path_list[:i])
        if os.path.exists(os.path.join(base_path, "repo.pth")):
            return os.path.realpath(os.path.join(base_path, '../'))
    raise AssertionError("Looks like you are not part of a Repo directory")


# path to e2e site under current repo
REPO_PATH = find_base_repo_path()

# addsitedir will not add duplicates into the sys.path
site.addsitedir(REPO_PATH + '/Traversals/')
