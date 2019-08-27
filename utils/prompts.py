from PyInquirer import prompt

def gitIdPrompt():
    questions = [
        {
            'type': 'input',
            'name': 'id',
            'message': 'Enter your github user id: ',
        },
        ]
    answer = prompt(questions)
    return answer['id']

def passwordPrompt():
    questions = [
        {
            'type': 'input',
            'name': 'password',
            'message': 'Enter your team encryption key: ',
        },
        ]
    answer = prompt(questions)
    return answer['password']

def setupPrompt():
    pass

def ownRepoPrompt():
    questions = [
        {
            'type': 'input',
            'name': 'my_repo',
            'message': 'Please enter your github empty repo link',
        },
    ]
    answer = prompt(questions)
    return answer['my_repo']

def teamKeyRepoPrompt():
    pass

def selectClusterPrompt(clusters):
    questions = [
        {
            'type': 'list',
            'name': 'cluster',
            'message': 'Select the cluster from the following list: ',
            'choices': clusters,
        }
    ]
    answer = prompt(questions)

    def processChoice(choice):
        for x, val in enumerate(clusters):
            if (val == choice):
                return x
        return -1

    return processChoice(answer['cluster'])


def mainMenuPrompt():
    '''
    1)List available clusters
    2)Create new cluster
    3)Quit
    '''
    options = ['List avaiable clusters','Create new cluster',
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
        if (operation == options[2]):
            return 2
            #installAddonPrompt()

    return processOps(answer['operation'])

def createNewClusterPrompt():

    pass

def welcomePrompt():
   print("Cluster manager initial run\n") 