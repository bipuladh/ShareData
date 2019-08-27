import os
import sys
import json

from utils.consts import OCS_DIR_PATH, OCS_CONFIG_FILE, OCS_INSTALL_PATH 


DEFAULT_CONFIG = {
            "REPO1":[
                {"URL": "https://github.com/operator-framework/operator-lifecycle-manager.git",
                "FILE": "deploy/deploy-with-olm.yaml"}
             ],
            "MYKEY":
                {"URL": "https://github.com/bipuladh/badhikar_ocs.git"},
            "EXTKEY01":
                {"URL":"https://github.com/bipuladh/badhikar_ocs.git"},
            "ENC_KEY":
                {"KEY":"changethis"},
            "GITID":"",
        }

def createConfiguration(configs = {} ):
    #Just create a dict and write it to json file
    if len(configs) == 0:
        configs = DEFAULT_CONFIG
    with open(OCS_CONFIG_FILE,"w") as file:
        json.dump(configs,file)

def checkAndCreate():
    if not os.path.exists(OCS_CONFIG_FILE):
        createConfiguration()

def loadConfigurations():
    checkAndCreate()
    config = ''
    with open( OCS_CONFIG_FILE, "r") as file:
        config = json.load(file)
    return config

def getRepos():
    config = loadConfigurations()
    external_repos = [config[key] for key in config if key.find('REPO') >= 0][0]
    internal_repo = [config[key] for key in config if key.find('MYKEY') >= 0]
    external_key_repos = [config[key] for key in config if key.find('EXT') >= 0]

    return external_repos, internal_repo, external_key_repos

