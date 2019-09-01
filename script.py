from PyInquirer import prompt, print_json
from utils.configurations import loadConfigurations
from utils.pull_secret_util import get_pull_secret
from utils.first_run import isFirstRun, performFirstRun
from utils.prompts import welcomeMessage, mainMenuPrompt, selectClusterPrompt
from utils.setupCluster import setupCluster
from utils.ClusterInquirer import ClusterInquirer
from utils.dateHandler import getAvailableClusters

'''
Tell the user that we are gonna setup a config file
'''

class Manager:
    def __init__(self):
        if isFirstRun():
            welcomeMessage()
            performFirstRun()
        self.configurations = loadConfigurations()
        self.clusterInquirer = ClusterInquirer(self.configurations)


    def setupCluster(self,selected):
        self.clusterInquirer.setupKube(selected)

    def createCluster(self):
        pass

    def getClustersStatus(self):
        return self.clusterInquirer.getStatus()
    
if __name__ == '__main__':
    #Declare a variable to maintain a program loop
    manager = Manager()
    while True:
        choice = mainMenuPrompt()
        if choice == 0:
            clusters = manager.getClustersStatus()
            healthyClusters = getAvailableClusters(clusters)
            selectedCluster = selectClusterPrompt( healthyClusters )
            manager.setupCluster(selectedCluster)
        if choice == 1:
            #Create a new cluster
            manager.createCluster()
        if choice == 2:
            break