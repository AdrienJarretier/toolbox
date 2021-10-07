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


def safeguardWord2(word):

    return random.choice([
        '♥censored-for-fragile-spirits-easily-offended♥',
        '♥censored-for-love♥',
        '♥this-is-not-a-bypass-of-the-censorship-filter♥',
        '♥censored-because-depth-of-vocabulary-is-overrated♥',
        '♥'+'-'.join(['heart' for _ in range(len(word)-2)])+'♥',
        '♥censored-because-I-don\'t-want-to-get-spanked♥',
        '♥I hope you do not consider "spanked" a profanity word♥',
        '♥hearts are peace, hearts are love♥',
    ]).replace(' ', '-')


def safeguardFile(filename):

    inFilePath = os.path.join(INPUT_DIR, filename)
    outFilePath = os.path.join(OUTPUT_DIR, filename)

    print(inFilePath)
    print(outFilePath)

    with open(inFilePath) as inFile:

        with open(outFilePath, 'w', encoding="utf-8") as outFile:

            for line in inFile:

                words = re.split('(\W)', line)
                for i in range(len(words)):

                    word = words[i]
                    if word in CENSOR_LIST:
                        words[i] = safeguardWord2(words[i])

                line = ''.join(words)

                outFile.write(line)


for filename in os.listdir(INPUT_DIR):

    if filename != '.gitignore':
        safeguardFile(filename)
