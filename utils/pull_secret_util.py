import os
from utils.consts import HOME_DIR_PATH, OCS_DIR_PATH, PULL_SECRET_ADDONS
from shutil import copyfile
import json


def get_pull_secret():
    #First check whether we have pull secret on 
    #Make sure the pull secret file is in home directory
    if not os.path.isfile( os.path.join(OCS_DIR_PATH,'pull-secret.txt') ):
        assert os.path.exists(os.path.join(HOME_DIR_PATH,"pull-secret.txt"))
        copyfile( os.path.join(HOME_DIR_PATH,"pull-secret.txt"),
            os.path.join(OCS_DIR_PATH,'pull-secret.txt') )
    verify_pull_secret()
    contents=''
    with open(os.path.join(OCS_DIR_PATH,"pull-secret.txt")) as file:
        contents = file.readlines()
    return contents

    

def verify_pull_secret():
    path = os.path.join(OCS_DIR_PATH, 'pull-secret.txt')
    file = open(path, 'r')
    data = json.load(file)

    if not 'registry.svc.ci.openshift.org' in data['auths']:
        data['auths']['registry.svc.ci.openshift.org'] = PULL_SECRET_ADDONS
    with open(path,'w') as file:
        json.dump(data,file)

    json.dumps(data)
