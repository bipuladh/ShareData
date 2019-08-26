from gitHelper import InternRepository
import os 
from consts import OCS_CACHE_PATH
from shutil import copyfile
import git
from utils import repo_name_from_url

MY_REPO = "https://github.com/bipuladh/badhikar_ocs.git"

repo = InternRepository(MY_REPO)
#repo.startRepo()

'''
try:
    _ = git.Repo().git_dir
except Exception:
    assert False
assert True
'''

#Copy something to that dir
#copyfile("/home/badhikar/testfile",os.path.join( OCS_CACHE_PATH,repo_name_from_url(MY_REPO),"testfile" ))
#repo.pushRepo()
