import pexpect
import os
from datetime import datetime as dt
from utils.consts import OCS_DIR_PATH, OCS_CLUSTERS_PATH, OCS_INSTALL_PATH
from utils.security import encryptString
import json
from utils.dateHandler import getTimeStamp
from threading import Thread

DATE_PATTERN ="%d.%m.%Y"
'''
specific cluster naming convention
<date according to pattern>-<kerberos_id>
'''


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

def getLocalUsableClusters():
        fresh = getLocalInstallations()
        return [ os.path.join(OCS_CLUSTERS_PATH,file) for file in fresh ]

#Gets the directory

def start_ocs_install(dir,ocs_path=OCS_INSTALL_PATH):
    #Might require a slash here check for errors
    CMD = ocs_path+"/openshift-install create cluster --dir " + dir
    child = pexpect.spawn(CMD, timeout=3600)
    #SSH select
    child.expect('SSH')
    child.interact("\r")
    child.sendline()
    #Platform select
    child.expect('Platform')
    child.interact("\r")
    child.sendline()
    #Region Select
    child.expect('Region')
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
    child.interact("\r")
    child.sendline()
    return child


class LocalClusterHandler:
        def __init__(self, repoManager, configuration):
                self.repoManager = repoManager
                self.configuration = configuration
                self.username = self.configuration['username']
                self.password = self.configuration['team_enc_key']

        def startInstallation(self):
                if not isFreshInstallAvailable(self.username):
                        self.updateStatus('CREATE')
                        self.createCluster(self.username)
                else:
                        print("Local Valid clusters already exist")
                        return self.getLocalUsableClusters()

                #Start installation
        def createCluster(self, username):
                date = dt.strftime(dt.today(), DATE_PATTERN)
                dir_name = date + '-' + username
                install_path = os.path.join( OCS_CLUSTERS_PATH, dir_name)
                if not os.path.exists(install_path):
                        os.mkdir(install_path)
                proc = start_ocs_install(install_path)
                authDir = os.path.join(install_path, 'auth')
                showInstallationMessages()
                thread = Thread(target = self.installationWatch, args = (proc, authDir) )
                thread.daemon = True
                thread.start()


        def installationWatch(self,process, authDir):
                process.expect(pexpect.EOF)
                print("\n\n\t\tInstallation Complete \t\t\n\n")
                self.updateStatus('RUN')
                self.addToRepo(authDir)



        def getLocalUsableClusters(self):
                return getLocalUsableClusters()

        def addToRepo(self,authDir):
                #Read file and pass the data to repoManager
                data = ''
                with open( os.path.join(authDir, 'kubeconfig') ) as file:
                        data = file.read()
                self.repoManager.updateMyRepo('kubeconfig', encryptString(self.password, data) )
                with open( os.path.join(authDir, 'kubeadmin-password')) as file:
                        data = file.read()
                self.repoManager.updateMyRepo('kubeadmin-password',encryptString(self.password, data) )
        
        def updateStatus(self,state):
                status = self.repoManager.getMyStatus()
                if len(status) == 0:
                        status['owner'] = self.username
                        status['status']  = 'CREATE'
                        status['creation_date'] = getTimeStamp()
                else:
                        if state == 'RUN':
                                status['status'] = 'RUN'
                        if state == 'DEAD':
                                status['status'] = 'DEAD'
                self.repoManager.updateMyRepo('status.json', json.dumps(status))


def showInstallationMessages():
        print("\nInstallation running in the background")
        print("\nTill then you can use other clusters or wait for your to create")
        print("\nDo not quit this program. Cluster creation process is handled by this process.")