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
            "EXTKEY01":{},
            "ENC_KEY":
                {"KEY":"changethis"},
            "GITID":"",
        }

def createConfiguration(configs = {} ):
    if len(configs) == 0:
        configs = DEFAULT_CONFIG
    return configs

def loadConfigurations():
    config = ''
    with open( OCS_CONFIG_FILE, "r") as file:
        config = json.load(file)
    return config

def writeConfigurations(config):
    with open(OCS_CONFIG_FILE, 'w') as file:
        json.dump(config, file)