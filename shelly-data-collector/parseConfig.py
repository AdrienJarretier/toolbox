import json

CONFIG_FILENAME = 'localConfig.json'


def askForList(endString):
    list = []
    e = ''
    while e != endString:
        e = input()
        list.append(e)

    list.pop()

    return list


def loadConfig():
    config = {}

    try:
        with open(CONFIG_FILENAME) as configFile:
            config = json.load(configFile)
    except FileNotFoundError:
        print('ips (one per line, end with 0) : ')
        ips = askForList('0')
        print(ips)

        # with open(CONFIG_FILENAME, 'w') as configFile:

    return config
