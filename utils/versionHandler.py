import os
from filesmgr import getRepos
from gitHelper import ExternRepository

def checkAndPullRepos():
    ext_repo, _, _ = getRepos()

    ext_rep_objs = [ ExternRepository(repo[0]['URL']) for repo in ext_repo ]
    [obj.pull() for obj in ext_rep_objs ]

    '''
    my_key_repo_obj = [InternRepository(repo_name_from_url(repo['URL'])) for repo in my_key_repo ]
    ext_key_repo_objs = [ExternRepository(repo['URL']) for repo in ext_key_repos ]
    '''
#checkAndPullRepos()
