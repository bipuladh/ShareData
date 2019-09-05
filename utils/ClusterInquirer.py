import os
from utils.repositories import initializeRepoManager
from utils.dateHandler import getHoursFromToday
from utils.kubeFileHandler import writeKube, writeKubePass

class ClusterInquirer:
    def __init__(self, configurations):
        self.manager = initializeRepoManager(configurations)

    def getStatus(self):
        statusList = self.manager.getExternalRepoStatus()
        viewList = []
        for item in viewList:
            obj = {}
            obj['owner'] = item['owner']
            obj['hours_elasped'] = getHoursFromToday(item['created_at'])
            obj['cluster_state'] = item['cluster_state']
            obj['remote'] = True
            statusList.append(obj)
        return statusList

    def setupKube(self, status):
        owner = status['owner']
        kubeconfig = self.manager.getExternalFile(owner,"kubeconfig")
        kubeadm = self.manager.getExternalFile(owner,"kubeadmin-password")
        writeKube(kubeconfig)
        writeKubePass(kubeadm)
    
    def setupLocalKube(self, path):
        authDir = os.path.join(path, 'auth')
        kubeconfig = ''
        kubeadmin_password = ''
        with open( os.path.join(authDir, 'kubeconfig'), 'r') as file:
            kubeconfig = file.read()
        with open( os.path.join(authDir, 'kubeadmin-password'), 'r') as file:
            kubeadmin_password = file.read()
        writeKube(kubeconfig)
        writeKubePass(kubeadmin_password)
        

    def getManager(self):
        return self.manager