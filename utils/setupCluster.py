import os
from shutil import copyfile
from utils.consts import OCS_KUBE_PATH
from utils.security import decryptfile

def setupSelectedCluster(clusterPath,password):
    auth_dir = os.path.join(clusterPath, 'auth')
    for file in os.listdir(auth_dir):
        if (str(file)).find('aes') == -1:
            #Not encrypted
            src = os.path.join(auth_dir, file)
            dest = os.path.join(OCS_KUBE_PATH, file)
            copyfile(src,dest)
        else:
            src = os.path.join(auth_dir, file)
            decryptfile(src,OCS_KUBE_PATH,password)