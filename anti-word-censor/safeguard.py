import os
import re
import string
import random

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

# print(os.listdir(INPUT_DIR))


def safeguardWord(word):

    wordChars = list(word)
    outputWord = ''
    for i in range(len(wordChars)-1):
        safetyChar = random.choice(
            ['', ' ', '.', random.choice(string.punctuation)])
        outputWord += wordChars[i]+safetyChar

    outputWord += wordChars[-1]
    return outputWord


def safeguardFile(filename):

    inFilePath = os.path.join(INPUT_DIR, filename)
    outFilePath = os.path.join(OUTPUT_DIR, filename)

    print(inFilePath)
    print(outFilePath)

    with open(inFilePath) as inFile:

        with open(outFilePath, 'w') as outFile:

            for line in inFile:

                words = re.split('(\W)', line)
                for i in range(len(words)):

                    word = words[i]
                    if word in CENSOR_LIST:
                        words[i] = safeguardWord(words[i])

                line = ''.join(words)

                outFile.write(line)


for filename in os.listdir(INPUT_DIR):

    if filename != '.gitignore':
        safeguardFile(filename)
