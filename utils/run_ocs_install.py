import pexpect
import os
from datetime import datetime as dt
from utils.consts import OCS_DIR_PATH, OCS_CLUSTERS_PATH, OCS_INSTALL_PATH
from utils.security import encryptfile
import json

DATE_PATTERN ="%d.%m.%Y"
'''
specific cluster naming convention
<date according to pattern>-<kerberos_id>
'''

def handleOcsInstallation(gitId, pullSecret,repoDir):
    #Check that no cluster is present today
    assert not isFreshInstallAvailable(gitId)
    #Create cluster directory
    create_cluster(gitId,pullSecret)
    addStatusToRepo(repoDir)


def isFreshInstallAvailable(gitId):
    date = dt.strftime(dt.today(), DATE_PATTERN)
    dir_name = date + '-' + gitId
    install_path = os.path.join( OCS_CLUSTERS_PATH, dir_name)
    if os.path.exists(install_path) :
            return True
    else:
            return False


def getLocalInstallations():
    dirs = os.listdir(OCS_CLUSTERS_PATH)
    freshInstalls = []
    for dir in dirs:
        date,_ = dir.split('-')
        creationDate = dt.strptime(date, DATE_PATTERN)
        diff = dt.today() - creationDate
        days = ( diff.total_seconds() )/ ( 60 * 60 * 45 )
        if days < 2:
            freshInstalls.append(dir)
    return freshInstalls

def getLocalUsableCluster():
        fresh = getLocalInstallations()
        return [ os.path.join(OCS_CLUSTERS_PATH,file) for file in fresh ]

#Gets the directory
def create_cluster(gitId, pullSecret):
    date = dt.strftime(dt.today(), DATE_PATTERN)
    dir_name = date + '-' + gitId
    install_path = os.path.join( OCS_CLUSTERS_PATH, dir_name)
    if not os.path.exists(install_path):
        os.mkdir(install_path)
    start_ocs_install(install_path, pullSecret)

'''
@param src_dir pass the auth directory else fails
@param repo_dir pass my repository
'''
def encryptAndAddToRepo(src_dir,repo_dir, password):
    for file in os.listdir(src_dir):
        src_file = os.path.join(src_dir,file)
        assert os.path.isfile(src_file)
        encryptfile(src_file, repo_dir,password)


'''
Add status file to repo
'''
def addStatusToRepo(repo_dir):
    status = {
        'CREATION_DATE':dt.today(),
        'STATUS':'RUN'
    }
    with open(os.path.join(repo_dir, 'state.json'), 'w') as file:
        json.dump(status,file)


def start_ocs_install(dir, pull_secret, ocs_path=OCS_INSTALL_PATH):
    #Might require a slash here check for errors
    CMD = ocs_path+"openshift-install create cluster --dir " + dir + "--log-level=debug"
    child = pexpect.spawn(CMD)
    #SSH select
    child.expect('SSH')
    child.interact("\r")
    child.sendline()
    #Platform select
    child.expect('Platform')
    child.interact("\r")
    child.sendline()
    #Region Select
    child.expect('Platform')
    child.interact("\r")
    child.sendline()
    #Base Domain
    child.expect('Base')
    child.interact("\r")
    child.sendline()
    #Cluter Name
    child.expect('Cluster')
    child.interact("\r")
    child.sendline()
    #Pull Secret
    child.expect('Pull')
    child.sendline(pull_secret)
    child.wait()