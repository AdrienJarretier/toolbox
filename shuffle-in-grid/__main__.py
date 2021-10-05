from texttable import Texttable
import random


COLS = 6

ELEMENTS_COUNT = 222

elements = list(range(1, ELEMENTS_COUNT+1))
random.shuffle(elements)

t = Texttable()
t.header(['', 'line', 'col'])
for i in range(ELEMENTS_COUNT):

    n = elements[i]

    lin = int(n/COLS)+1
    col = 1+(n-1) % COLS

    t.add_row([n, lin, col])

print(t.draw())
