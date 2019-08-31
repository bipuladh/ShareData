import json
from datetime import datetime as dt
import os

'''
 key_file_data => {
     'CREATION_DATE':<date>,
     'STATUS':'CREATE | RUN | DEAD'
 }
'''

CREATE = "CREATE"
RUN = "RUN"
DEAD = "DEAD"

DATE_PATTERN = "%Y/%m/%d-%H:%M:%S"


def getHoursFromToday(timestamp):
    date = dt.strptime(timestamp, DATE_PATTERN)
    diff = dt.today() - date
    hours = diff.total_seconds() / 3600
    return hours

def getTimeStamp():
    return dt.today().strftime(DATE_PATTERN)

'''
Path is the path to json file containing cluster_state_info
@returns (usable:bool, hours_left:float)
'''
def checkKeyCreationDate(path):
    data = {}
    try:
        with open(path,'r') as file:
            data = json.load(file)
    except Exception:
        assert False
    creationDate =dt.strptime(data['CREATION_DATE'],DATE_PATTERN)
    status = data['STATUS']

    if status == RUN:
        now = dt.now()
        seconds = ( now - creationDate).total_seconds()
        hours = (seconds / 60) / 60
        if (hours > 45 ):
            status = DEAD
        else:
            return True, (48 - hours)

    if status == DEAD:
        return False, 0

    if status == CREATE:
        return False, 48

'''
Return a list of usable clusters and loading clusters
@param key_repos : A list of paths to the clusters
@param json_file : Name of the json file
'''
def getUsableExternalClusters(keyRepos=[], fileName='state.json'):
    if len(keyRepos) == 0:
        keyRepos = getTeamDirs()
    usableClusters = []
    loadingClusters = []
    for repoDir in keyRepos:
        file = os.path.join( repoDir, fileName)
        if not os.path.exists(file):
            continue
        state, hrsLeft = checkKeyCreationDate(file)
        if (state == True):
            usableClusters.append(repoDir)
        if state == False and hrsLeft > 0:
            loadingClusters.append(repoDir)
    return usableClusters, loadingClusters   

def getTeamDirs():
    return []