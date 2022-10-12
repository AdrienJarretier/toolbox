import itertools
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
        for i in range(len(CENSOR_LIST)):
            CENSOR_LIST[i] = CENSOR_LIST[i].lower()
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


funnyStrings = [
    '♥censored-for-delicate-spirits♥'
    '♥censored-for-love♥',
    '♥this-is-not-a-bypass-of-the-censorship-filter♥',
    '♥censored-because-depth-of-vocabulary-is-overrated♥',
    '♥censored-because-I-don\'t-want-to-get-spanked♥',
    '♥I hope you do not consider "spanked" a profanity word♥',
    '♥hearts are peace, hearts are love♥',
]
funnyStringsWeights = [1]*(len(funnyStrings)+1)


def replaceWithFunnyString(word):

    cumulativeWeigths = list(itertools.accumulate(funnyStringsWeights))

    pick = random.randint(1, cumulativeWeigths[-1])
    pickedIndex = 0
    while cumulativeWeigths[pickedIndex] < pick:
        pickedIndex += 1

    for i in range(len(funnyStringsWeights)):
        funnyStringsWeights[i] += 2

    funnyStringsWeights[pickedIndex] = 1

    return (funnyStrings
            + [
                '♥' +
                '-'.join(['heart']*(len(word)-2))+'♥'
            ]
            )[pickedIndex].replace(' ', '-')


def safeguardFile(filename):

    inFilePath = os.path.join(INPUT_DIR, filename)
    outFilePath = os.path.join(OUTPUT_DIR, filename)

    print(inFilePath)
    print(outFilePath)

    with open(inFilePath, encoding="utf-8") as inFile:

        with open(outFilePath, 'w', encoding="utf-8") as outFile:

            for line in inFile:

                words = re.split('(\W)', line)
                for i in range(len(words)):

                    word = words[i]
                    if word.lower() in CENSOR_LIST:
                        words[i] = replaceWithFunnyString(words[i])

                line = ''.join(words)

                outFile.write(line)


for filename in os.listdir(INPUT_DIR):

    if filename != '.gitignore':
        safeguardFile(filename)
