from git import Repo, GitCommandError
from utils.consts import REPO_NAME
from datetime import date
import os
from utils.utils import repo_name_from_url
from shutil import copyfile
from github import Github



class Repository:
    def __init__( self, username, password):
        self.username = username
        self.gitUser = Github(username, password)


class ExternRepository(Repository):

    def __init__(self, username, password, externalUser):
        super(username,password)
        repo_name = externalUser + "/" + REPO_NAME
        self.repo = self.gitUser.get_repo(repo_name)

    def getStatus(self):
        status = self.repo.get_contents("status.json")
        return status.content
    
    def getFile(self, fileName):
        contents = self.repo.get_contents(fileName)
        return contents


class InternalRepository(Repository):

    def __init__(self,username,password):
        super(username, password)
        repo_name = username + "/" + REPO_NAME
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
        filePath = "/{}".format(filename)
        contents = self.repo.get_contents(filePath)
        commit_msg = "Updated file {}".format(filename) 
        self.repo.update_file(contents.path, commit_msg, data, contents.sha)

    def createFile(self, filename, data):
        filePath = "/{}".format(filename)
        commit_msg = "Created file {}".format(filename)
        self.repo.create_file(filePath, commit_msg, data)