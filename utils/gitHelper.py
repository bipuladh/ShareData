from utils.consts import REPO_NAME
from github import Github
import json
from utils.security import decryptByte



class Repository:
    def __init__( self, username, password):
        self.username = username
        self.gitUser = Github(username, password)


class ExternRepository(Repository):
    def __init__(self, username, password, externalUser, teamEncKey):
        super(ExternRepository,self).__init__(username, password)
        repo_name = externalUser + "/" + REPO_NAME
        self.repo = self.gitUser.get_repo(repo_name)
        self.teamEncKey = teamEncKey

    def getStatus(self):
        status = self.repo.get_contents("status.json")
        return status.decoded_content

    def getFile(self, fileName):
        contents = self.repo.get_contents(fileName)
        if not type(contents.decoded_content) == str:
            return decryptByte(self.teamEncKey, contents.decoded_content)
        else:
            return contents.decoded_content
    
    def getOwner(self):
        return (self.repo.owner).login

class InternalRepository(Repository):
    def __init__(self,username,password):
        super(InternalRepository,self).__init__(username, password)
        repo_name = username + "/" + REPO_NAME
        try:
            self.repo = self.gitUser.get_repo(repo_name)
        except Exception:
            usr = self.gitUser.get_user()
            usr.create_repo(REPO_NAME)
            self.repo = self.gitUser.get_repo(repo_name)

    def addFile(self, filename, data):
        doesExist = False
        filePath = "/{}".format(filename)
        try:
            self.repo.get_contents(filePath)
            doesExist = True
        except Exception:
            pass
        if doesExist:
            self.updateFile(filename, data)
        else:
            self.createFile(filename, data)

    def updateFile(self, filename, data):
        filePath = "{}".format(filename)
        contents = self.repo.get_contents(filePath)
        commit_msg = "Updated file {}".format(filename) 
        self.repo.update_file(contents.path, commit_msg, data, contents.sha)

    def createFile(self, filename, data):
        filePath = "{}".format(filename)
        commit_msg = "Created file {}".format(filename)
        self.repo.create_file(filePath, commit_msg, data)

    def getStatus(self):
        file = {}
        try:
            file = self.repo.get_contents("status.json")
            file = file.decoded_content
            file = json.loads(file)
        except Exception:
            pass
        return file