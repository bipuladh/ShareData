import os
import sys
import json
from utils.consts import OCS_DIR_PATH, OCS_CONFIG_FILE 

DEFAULT_CONFIG = {
        "username": "",
        "password": "",
        "friends_git_id":['messi199610'],
    }

def writeConfigurations(config):
    with open(OCS_CONFIG_FILE, 'w') as file:
        json.dump(config, file)

def loadConfigurations():
    config = ''
    with open(OCS_CONFIG_FILE, 'r') as file:
        config = json.load(file)
    return config