from utils.gitHelper import ExternRepository, InternalRepository
import json

class RepositoryManager:

    def __init__(self, myRepo, externalRepos = [] ):
        self.myRepo = myRepo
        self.externalRepos = externalRepos

    def updateMyRepo(self, filename, data):
        self.myRepo.addFile(filename, data)
    
    def getMyStatus(self):
        return self.myRepo.getStatus()

    def getExternalFile(self, owner, filename):
        for repo in self.externalRepos:
            if repo.getOwner() == owner:
                return repo.getFile(filename)
        raise Exception("No owner found")

    def getExternalRepoStatus(self):
        statusList = []
        for repo in self.externalRepos:
            status = json.loads(repo.getStatus())
            statusList.append(status)
        
        return statusList

def initializeRepoManager(configurations):
    username = configurations['username']
    password = configurations['password']
    watchedRepo = configurations['friends_git_id']
    team_enc_key = configurations['team_enc_key']

    def createMyRepoObject(username, password):
        return InternalRepository(username, password)

    def createOtherRepo(username, password, id):
        return ExternRepository(username, password, id, team_enc_key)

    myRepo = createMyRepoObject(username, password)
    extRepos = []
    for repo in watchedRepo:
        extRepo = createOtherRepo(username, password, repo)
        extRepos.append(extRepo)

    return RepositoryManager(myRepo, extRepos)