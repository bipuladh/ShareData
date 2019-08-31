import os
from utils.consts import OCS_DIR_PATH, OCS_CLUSTERS_PATH, OCS_CACHE_PATH, OCS_KUBE_PATH, HOME_DIR_PATH
from utils.filesmgr import loadConfigurations, createConfiguration 
from utils.versionHandler import updateInternalRepo

def isFirstRun():
    if not os.path.exists(OCS_DIR_PATH):
        return True
    else:
        return False

def performFirstRun(my_repo_url, enc_key, gitId, list_ext_repos=[]):
    setupDirectories()
    setupKubeconfig()
    config = loadConfigurations()
    config['MYKEY']['URL'] = my_repo_url
    config['ENC_KEY']['KEY'] = enc_key
    config["GITID"] = gitId

    for count,repo in enumerate(list_ext_repos):
        config['EXTKEY0' + str(count)] = {}
        config['EXTKEY0' + str(count)]['URL'] = repo

    createConfiguration(config)
    #Create the ocs_data/cluster directory
    #Setup the repo now
    updateInternalRepo()


def setupDirectories():
    if not os.path.exists(OCS_DIR_PATH):
        os.mkdir(OCS_DIR_PATH)
    if not os.path.exists(OCS_CLUSTERS_PATH):
        os.mkdir(OCS_CLUSTERS_PATH)
    if not os.path.exists(OCS_CACHE_PATH):
        os.mkdir(OCS_CACHE_PATH)
    if not os.path.exists(OCS_KUBE_PATH):
        os.mkdir(OCS_KUBE_PATH)

def setupKubeconfig():
    line = "export KUBECONFIG=" + OCS_KUBE_PATH + "/kubeconfig"
    with open(os.path.join(HOME_DIR_PATH,'.bashrc'),'a') as file:
        file.write(line)

    
