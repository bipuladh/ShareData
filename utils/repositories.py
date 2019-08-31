from git import Repo, GitCommandError
from utils.consts import OCS_CACHE_PATH
from datetime import date
import os
from shutil import copyfile

class RepositoryManager:

    def __init__(self, myRepo, externalRepos = [] ):
        self.myRepo = myRepo
        self.externalRepos = externalRepos

    def updateMyRepo(self, filename, data):
        self.myRepo.addFile(filename, data)

    def getMyFile(self, filename, data):
        pass

    def getExternalFile(self, filename, data):
        pass
