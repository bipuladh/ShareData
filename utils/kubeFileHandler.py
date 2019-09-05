from utils.consts import KUBE_PATH
from os import path

KUBE_CONFIG_FILE = path.join(KUBE_PATH,'kubeconfig')
KUBE_PASS_FILE = path.join(KUBE_PATH,'kubeadmin-password')

def writeKube(data):
    with open(KUBE_CONFIG_FILE,'w') as file:
        file.write(data)

def readFromKube():
    data = ''
    with open(KUBE_CONFIG_FILE, 'r') as file:
        data = file.readlines()
    return data

def readKubePass():
    data = ''
    with open(KUBE_PASS_FILE, 'r') as file:
        data = file.readlines()
    return data

def writeKubePass(kubepass):
    with open(KUBE_PASS_FILE,'w') as file:
        file.write(kubepass)