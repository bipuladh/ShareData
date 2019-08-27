from utils.versionHandler import checkAndPullDataRepos, getTeamDirs
import os
from utils.keyVersionHandler import getUsableClusters

def startMonitoringKeyRepos():
    dirs = getTeamDirs()
    usable, loading = getUsableClusters(dirs)
    return usable, loading

def startMonitoringOtherRepos():
    checkAndPullDataRepos()

