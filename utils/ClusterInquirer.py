import os
from utils.repositories import initializeRepoManager
from utils.dateHandler import getHoursFromToday

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

    def setupKube(self, owner):
        pass