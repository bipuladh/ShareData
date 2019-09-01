import os
from utils.consts import KUBE_PATH
from utils.kubeFileHandler import writeKubePass, writeKube

def setupCluster(kubeconfig, kubepass):
    writeKube(kubeconfig)
    writeKubePass(kubepass)