import os
from utils.consts import OCS_DIR_PATH, KUBE_PATH, HOME_DIR_PATH
from utils.configurations import DEFAULT_CONFIG, writeConfigurations
from utils.prompts import getGitInformation, teamGitIdPrompt

def isFirstRun():
    if not os.path.exists(OCS_DIR_PATH):
        return True
    else:
        return False

def performFirstRun():
    setupDirectories()
    setupKubeconfig()
    username, password = getGitInformation()
    userList = teamGitIdPrompt()
    setupConfigurations( username, password, userList)

def setupConfigurations(gitUsername, gitPassword, userList):
    config = DEFAULT_CONFIG
    config['username'] = gitUsername
    config['password'] = gitPassword
    config['friends_git_id'] = userList
    writeConfigurations(config)

def setupDirectories():
    if not os.path.exists(OCS_DIR_PATH):
        os.mkdir(OCS_DIR_PATH)
    if not os.path.exists(KUBE_PATH):
        os.mkdir(KUBE_PATH)

def setupKubeconfig():
    line = "export KUBECONFIG=" + KUBE_PATH + "/kubeconfig"
    with open(os.path.join(HOME_DIR_PATH,'.bashrc'),'a') as file:
        file.write(line)