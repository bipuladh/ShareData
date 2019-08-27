import os
from utils.filesmgr import getRepos
from utils.gitHelper import ExternRepository,InternRepository

def checkAndPullDataRepos():
    ext_repo, _, _ = getRepos()

    ext_rep_objs = [ ExternRepository(repo['URL']) for repo in ext_repo ]
    [obj.pull() for obj in ext_rep_objs ]

def updateInternalRepo():
    _, my_key,_ = getRepos()
    my_repo = InternRepository(my_key[0]['URL'])
    my_repo.pushRepo()

def updateExternalKeyRepos():
    _,_,team_keys = getRepos()
    if len(team_keys) > 0:
        team_rep_objs = [ExternRepository(repo['URL']) for repo in team_keys]
        [obj.pull() for obj in team_rep_objs]

def getTeamDirs():
    _,_,team_keys = getRepos()
    team_rep_objs = [ExternRepository(repo['URL']) for repo in team_keys]
    [obj.pull() for obj in team_rep_objs]
    team_dirs = [obj.getPath() for obj in team_rep_objs]
    return team_dirs

def getMyRepoPath():
    _,my_key,_ = getRepos()
    my_repo = InternRepository( my_key[0]['URL'] )
    return my_repo.getPath()