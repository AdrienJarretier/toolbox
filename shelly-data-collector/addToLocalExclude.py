
def addToLocalExclude(path):
    with open('../.git/info/exclude', 'r+') as excludeF:

        if excludeF.readlines()[-1][-1] != '\n':
            excludeF.write('\n')

        excludeF.write(path)
        excludeF.write('\n')
