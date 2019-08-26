import pexpect

def start_ocs_install(dir, pull_secret, ocs_path="/home/badhikar/openshift-install/"):
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