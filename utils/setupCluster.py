import os
from utils.consts import KUBE_PATH
from utils.kubeFileHandler import writeKubePass, writeToKube

def setupCluster(kubeconfig, kubepass):
    writeToKube(kubeconfig)
    writeKubePass(kubepass)