from PyInquirer import prompt, print_json
from utils.filesmgr import loadConfigurations
from utils.keyVersionHandler import getUsableExternalClusters
from utils.run_ocs_install import getLocalUsableCluster, handleOcsInstallation
from utils.pull_secret_util import get_pull_secret
from utils.first_run import isFirstRun, performFirstRun
from utils.regular_run import performUpdates
from utils.versionHandler import getMyRepoPath
from utils.prompts import *
from utils.setupCluster import setupSelectedCluster

'''
Tell the user that we are gonna setup a config file
'''

class Manager:
    def __init__(self):
        #Check for first run
        if isFirstRun():
            #Just prints msg
            welcomePrompt()
            #Repo github url
            self.my_repo_url = ownRepoPrompt()
            #Passowrd detail
            self.enc_key = passwordPrompt()
            #Github id
            self.gitId = gitIdPrompt()
            #Creates a configuration file and initalizes my repo if not initialized
            performFirstRun(self.my_repo_url, self.enc_key,self.gitId)
        else:
            #Configuration
            self.config = loadConfigurations()
            #my repository url
            self.my_repo_url = self.config['MYKEY']['URL']
            self.enc_key = self.config['ENC_KEY']['KEY']
            self.gitId = self.config['GITID']
            #Update the external repositories
            performUpdates()
        #My repository for files
        self.repo_path = getMyRepoPath()
        #Configurations 
        self.config = loadConfigurations() 
        #My personal clusters
        self.localCluster = getLocalUsableCluster()
        self.pullSecret = get_pull_secret()
        self.extUsables, _ = getUsableExternalClusters()
        self.myCluster = ''

    def getClusterLists(self):
        return self.extUsables + self.localCluster

    def getInternalClusters(self):
        return self.localCluster
    
    def getPassword(self):
        return self.enc_key
    
    #This one is a complicated process handled by the method below
    def createCluster(self):
        if len( self.localCluster ) == 0:
            #Create a local cluster
            handleOcsInstallation(self.gitId, self.pullSecret, self.repo_path)


if __name__ == '__main__':
    #Declare a variable to maintain a program loop
    manager = Manager()
    while True:
        choice = mainMenuPrompt()
        if choice == 0:
            clusters = manager.getClusterLists()
            selected = selectClusterPrompt( clusters )
            setupSelectedCluster(clusters[selected], manager.getPassword())
        if choice == 1:
            #Create a new cluster
            manager.createCluster()
        if choice == 2:
            break