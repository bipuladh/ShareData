from PyInquirer import prompt
from utils.dateHandler import getHoursFromToday

def getGitInformation():
    username, password, enc_key = gitPrompt()
    return username, password, enc_key

def gitPrompt():
    questions = [
        {
            'type': 'input',
            'name': 'id',
            'message': 'Enter your github user name: ',
        },
        {
            'type': 'password',
            'name': 'password',
            'message': 'Enter your github password: ',
        },
        {
            'type': 'password',
            'name': 'enc_key',
            'message': 'Enter your team enycrption key: ',
        }
        ]
    answer = prompt(questions)
    return answer['id'], answer['password'], answer['enc_key']

def localClustersPrompt(clusters):
    choices = [ ' Creation Date = {} '.format(cluster) 
        for cluster in clusters]
    questions = [
        {
            'type': 'list',
            'name': 'cluster',
            'message': 'Select the cluster from the following list: ',
            'choices': choices,
        }
    ]
    answer = prompt(questions)

    def processChoice(choice):
        for x, val in enumerate(choices):
            if (val == choice):
                return x
        return -1

    indexSelected = processChoice( answer['cluster'] )
    return clusters[ indexSelected ]


def teamGitIdPrompt():
    def askUserToAddGitUsers(msg):
        question = {
            'type': 'confirm',
            'message': msg,
            'name': 'add',
            'default': False,
        }
        ans = prompt(question)
        return ans['add']
    
    def askAddGitUsers():
        questions = [
            {
                'type':'input',
                'name':'gitId',
                'message':'Enter your team member\'s git id: '
            },
        ]
        answer = prompt(questions)
        return answer['gitId']

    confirmFirst = 'Do you want to enter git id of your team member? '
    confirm = 'Do you want to enter another git id of your team member? '

    userList = []

    if askUserToAddGitUsers(confirmFirst):
        while True:
            userList.append(askAddGitUsers())
            if not askUserToAddGitUsers(confirm):
                break
    
    return userList

def selectClusterPrompt(clusters):
    choices = [ 'Owner = {} || Status = {} || Time-left = {} hours'.format(cluster['owner'], cluster['status'],
         48 - getHoursFromToday( cluster['creation_date']) ) 
        for cluster in clusters]
    questions = [
        {
            'type': 'list',
            'name': 'cluster',
            'message': 'Select the cluster from the following list: ',
            'choices': choices,
        }
    ]
    answer = prompt(questions)

    def processChoice(choice):
        for x, val in enumerate(choices):
            if (val == choice):
                return x
        return -1

    indexSelected = processChoice( answer['cluster'] )
    return clusters[ indexSelected ]


def mainMenuPrompt(showLocalClusters):
    '''
    1)List available clusters
    2)Create new cluster
    3)Quit
    '''

    options = ['List avaiable clusters','Create new cluster',
        'Quit']

    if showLocalClusters:
        options = ['List avaiable clusters', 'Create new cluster','Show local clusters',
            'Quit']

    questions = [
        {
            'type': 'list',
            'name': 'operation',
            'message': 'What do you want to do',
            'choices': options,

        }
    ]
    answer = prompt(questions)

    def processOps(operation):
        if (operation == options[0]):
            return 0
        if (operation == options[1]):
            return 1
            #createNewClusterPrompt()
        if (operation == 'Show local clusters'):
            return 2
            #installAddonPrompt()
        if (operation == 'Quit'):
            return 3
        

    return processOps(answer['operation'])

def createNewClusterPrompt():
    pass

def welcomeMessage():
   print("\n\t\tCluster manager initial run\n") 