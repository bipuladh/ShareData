from filesmgr import loadConfigurations, getRepos

if __name__ == "__main__":
    configs = loadConfigurations()
    #print(configs)

    ext, inter, key  = getRepos()
    ext_rep_objs = [ (repo['URL']) for repo in ext ]
    inter_obj = [ (repo['URL']) for repo in inter ]
    key_objs = [ (repo['URL']) for repo in key ]
    print(ext_rep_objs)
    print(inter_obj)
    print(key_objs)