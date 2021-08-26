import random
import re
import pprint

# with open(textFile) as f:
#     text = f.read()
#     print(len(text))

#     MIN_QUOTE_LEN = 2
#     print(text[len(text)-MIN_QUOTE_LEN:len(text)])

#     for i in range(1):
#         quoteStart = random.randint(0,len(text)-MIN_QUOTE_LEN)
#         quoteLen = random.randint(MIN_QUOTE_LEN,280)
#         quoteEnd = min(len(text), quoteStart+quoteLen)
#         print(text[quoteStart:quoteEnd])


def getWordsStarts(text):

    wordsStarts = [0]
    for i in range(len(text)):
        c = text[i]
        if re.match('\s', c) and not re.match('\s', text[i+1]):
            wordsStarts.append(i+1)

    return wordsStarts


def testGetWordsStarts(text):
    wordsStarts = getWordsStarts(text)
    for i in range(len(wordsStarts)):
        s = wordsStarts[i]
        e = wordsStarts[i+1]-1 if i+1 < len(wordsStarts) else len(text)
        print(s, text[s:e])


def getQuote(text):
    wordsStarts = getWordsStarts(text)
    pickedWordStart = random.randint(0, len(wordsStarts)-1)

    quoteStart = wordsStarts[pickedWordStart]

    pickedWordEnd = random.randint(pickedWordStart+1, len(wordsStarts))

    if pickedWordEnd < len(wordsStarts):
        quoteEnd = wordsStarts[pickedWordEnd]
    else:
        quoteEnd = len(text)

    return text[quoteStart:quoteEnd]


textFile = 'test.txt'
with open(textFile) as f:
    text = f.read()

    quotes = {}
    
    for _ in range(10000):
        q = getQuote(text)
        if q not in quotes:
            quotes[q] = 0
        quotes[q] += 1

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(quotes)
    
