import json

from addToLocalExclude import addToLocalExclude

CONFIG_FILENAME = 'localConfig.json'


def askForList(endString):
    list = []
    e = ''
    print('(one per line, end with '+endString+') :')
    while e != endString:
        e = input()
        list.append(e)

    list.pop()

    return list


def askForInt():
    return int(eval(input()))

def askForString():
    return input()


def askForDict(dic, depth=0):

    for k in dic:

        v = dic[k]

        print('  '*depth + k + ' ', end='')
        if isinstance(v, dict):
            print()
            dic[k] = askForDict(v, depth+1)
        elif isinstance(v, list):
            dic[k] = askForList('0')
        elif isinstance(v, int):
            dic[k] = askForInt()
        elif isinstance(v, str):
            dic[k] = askForString()

        # print(k)

    return dic

def addOutputFoldersToLocalExclude(config):
    for k in config:
        if 'outputFolder' in config[k]:
            addToLocalExclude('shelly-data-collector/'+config[k]['outputFolder']+'/**')

def loadConfig():
    config = {}

    try:
        with open(CONFIG_FILENAME) as configFile:
            config = json.load(configFile)
    except FileNotFoundError:
        with open('templateLocalConfig.json') as configTemplate:
            config = askForDict(json.load(configTemplate))
            with open(CONFIG_FILENAME, 'w') as configFile:
                json.dump(config, configFile, indent=4)
            addOutputFoldersToLocalExclude(config)

    return config