import os
import re

INPUT_DIR = 'inputs'
OUTPUT_DIR = 'outputs'

CENSOR_LIST_FILENAME = 'censorList.txt'

try:
    with open(CENSOR_LIST_FILENAME) as inFile:
        censorListContent = inFile.read()
        CENSOR_LIST = censorListContent.split()
except FileNotFoundError:
    print('missing censor list file :')
    print('Add ' + CENSOR_LIST_FILENAME)
    exit()


print(CENSOR_LIST)


# print(os.listdir(INPUT_DIR))


filename = os.path.join(INPUT_DIR, 'test.txt')
outFilename = os.path.join(OUTPUT_DIR, 'test.txt')

with open(filename) as inFile:

    with open(outFilename, 'w') as outFile:

        for line in inFile:

            words = re.split('(\W)', line)
            for i in range(len(words)):

                word = words[i]
                if word in CENSOR_LIST:
                    words[i] = '.'.join(list(word))

            line = ''.join(words)

            outFile.write(line)


# for file in os.listdir(INPUT_DIR):
