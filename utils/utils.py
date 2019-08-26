import os
import git

def get_dirs_from_path(path):
    assert os.path.exists(path)
    contents = os.listdir(path)
    dir = []
    for item in contents:
        item_path = os.path.join(path, item)
        if os.path.isdir( item_path ):
            dir.append(item_path)
    return dir

#https://stackoverflow.com/questions/19687394/python-script-to-determine-if-a-directory-is-a-git-repository
def is_git(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except Exception:
        return False

def repo_name_from_url(url):
    pathname, _=  ( url.split('/')[-1] ).split('.')
    return pathname


