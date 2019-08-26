from gitHelper import ExternRepository
from consts import OCS_CACHE_PATH
from filesmgr import loadConfigurations
import os

configs = loadConfigurations()
ext = ExternRepository(url=configs['REPO1']['URL'])
ext.pull()

pathname, _=  ( configs['REPO1']['URL'].split('/')[-1] ).split('.')
assert os.path.exists( os.path.join(OCS_CACHE_PATH, pathname) )