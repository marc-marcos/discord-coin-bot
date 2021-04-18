# Manual way of editing the data.json without the need of the Discord Bot

import json


def deleteAccount(account):
    f = open('data.json')
    data = json.load(f)
    f.close()

    del data[str(account)]

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
    
def changeValue(account, newValue):
    f = open('data.json')
    data = json.load(f)
    f.close()

    data[str(account)] = int(newValue)

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

def addAccount(account):
    f = open('data.json')
    data = json.load(f)
    f.close()

    data[str(account)] = 0

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

def deleteAll():
    f = open('data.json')
    data = json.load(f)
    f.close()

    storage = []
    for i in data:
        storage.append(i)
    
    for i in storage:
        del data[i]

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)


while True:
    print('Choose one of the following options: Delete Account, Change Value, Add Account, Delete All [1-4]')
    choice = input('>>> ')

    if int(choice) == 1:
        print('\nSpecify the account you want to delete')
        inp = input('>>> ')
        deleteAccount(inp)

    if int(choice) == 2:
        print('\n Specify, in that order, the account and the value you want to change')
        inp = input('>>> ')
        inp2 = input('>>> ')

        changeValue(inp, inp2)

    if int(choice) == 3:
        print('\n Specify the account you want to add')
        inp = input('>>> ')
        addAccount(inp)

    if int(choice) == 4:
        deleteAll()