from PyInquirer import prompt, print_json
from utils.configurations import loadConfigurations
from utils.pull_secret_util import get_pull_secret
from utils.first_run import isFirstRun, performFirstRun
from utils.prompts import welcomeMessage, mainMenuPrompt, selectClusterPrompt, localClustersPrompt
from utils.setupCluster import setupCluster
from utils.ClusterInquirer import ClusterInquirer
from utils.dateHandler import getAvailableClusters
from utils.run_ocs_install import LocalClusterHandler

class Manager:
    def __init__(self):
        if isFirstRun():
            welcomeMessage()
            performFirstRun()
        self.configurations = loadConfigurations()
        self.clusterInquirer = ClusterInquirer(self.configurations)
        self.LocalClusterHandler = LocalClusterHandler(self.clusterInquirer.getManager(),
            self.configurations)


    def setupCluster(self,selected, local=False):
        if not local:
            self.clusterInquirer.setupKube(selected)
        else:
            self.clusterInquirer.setupLocalKube(selected)

    def createCluster(self):
        self.LocalClusterHandler.startInstallation()

    def getClustersStatus(self):
        return self.clusterInquirer.getStatus()
    
if __name__ == '__main__':
    #Declare a variable to maintain a program loop
    manager = Manager()
    showLocalClusters = False
    while True:
        localClusters = manager.LocalClusterHandler.getLocalUsableClusters()
        if len(localClusters) > 0 :
            showLocalClusters=True
        choice = mainMenuPrompt(showLocalClusters)
        #List available clusters
        if choice == 0:
            #Get all clusters
            clusters = manager.getClustersStatus()
            healthyClusters = getAvailableClusters(clusters)
            selectedCluster = selectClusterPrompt( healthyClusters )
            manager.setupCluster(selectedCluster)
            print("The selected cluster has been setup")
        # Create new cluster
        if choice == 1:
            manager.createCluster()
        #Show local clusters
        if choice == 2:
            #Selected cluster is the path to cluster
            selectedCluster = localClustersPrompt(localClusters)
            manager.setupCluster(selectedCluster, local=True)
            print("Local cluster is setup!")
        # Quit
        if choice == 3:
            break