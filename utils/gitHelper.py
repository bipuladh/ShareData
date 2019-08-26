from git import Repo, GitCommandError
from consts import OCS_CACHE_PATH
from datetime import date
import os
from utils import repo_name_from_url
from shutil import copyfile


class ExternRepository:

    def __init__(self, url):
        self.url = url
        self.pull()

    def pull(self):
        pathname, _=  ( self.url.split('/')[-1] ).split('.')
        self.path = os.path.join(OCS_CACHE_PATH, pathname)
        if os.path.exists( self.path ):
            self.repo = Repo(self.path)
            origin = self.repo.remotes.origin
            origin.pull()
        else:
            self.repo = Repo.clone_from(self.url, self.path )
    
    def getPath(self):
        return self.path


class InternRepository:

    def __init__(self,url):
        self.url = url
        self.path = os.path.join(OCS_CACHE_PATH,repo_name_from_url(self.url))
        self.__startRepo__()

    def __startRepo__(self):
        #First check if
        if not os.path.exists(self.path):
            #Only run the first time important
            os.mkdir(self.path)
            self.repo = Repo.clone_from(self.url, self.path)
            #self.repo.create_head('master')
            #Touch a file
            try:
                open( os.path.join(self.path, "README.md"), "a" ).close()
            except Exception:
                assert False
            self.repo.git.add(update=True)
            self.repo.index.commit( str(date.today() ))
            self.repo.remotes.origin.push()
        else:
            self.repo = Repo(self.path)
            origin = self.repo.remotes.origin
            self.repo.create_head('master',origin.refs.master)
            self.repo.heads.master.set_tracking_branch(origin.refs.master)
            self.repo.heads.master.checkout()
            origin.fetch()
            origin.pull()

    def getPath(self):
        return self.path

    def addFiles(self,path,push=False):
        copyfile(path, self.path)
        if push:
            self.pushRepo()

    def pushRepo(self):
        try:
            origin = self.repo.remotes.origin
            self.repo.heads.master.set_tracking_branch(origin.refs.master)
            self.repo.heads.master.checkout()
            origin.fetch()
            origin.pull()
            self.repo.git.add(update=True)
            self.repo.index.commit( str( date.today() ) )
            origin.push()
        except GitCommandError as e:
            print(e)
    