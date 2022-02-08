
import fractions
from functools import reduce
import math

n = 12

totalLeaves = math.factorial(n)
print('totalLeaves :', totalLeaves)
previousProgress = 0

def tree(signs, h = -1, drawn = None, successes=0, successesCount = None):

    successesCount = successesCount or [0]*(len(signs)+1)

    if h==drawn:
        successes+=1

    # print('\t'*h, signs, drawn, successes)

    if len(signs) == 0:
        successesCount[successes] += 1

        leaves = reduce(lambda x,y: x+y, successesCount)
        progress = leaves/totalLeaves

        global previousProgress
        if progress-previousProgress > 0.01:
            print('')
            print('progress :', leaves/totalLeaves, end='\r')
            previousProgress = progress
        # print('\t'*h, successesCount)

    else:
        for i in range(len(signs)):

            drawn = signs[i]

            signsCopy = signs.copy()
            del signsCopy[i]

            tree(signsCopy, h+1, drawn, successes, successesCount)

        return successesCount





signs = [i for i in range(n)]
successesCount = tree(signs)
print(successesCount)

leaves = reduce(lambda x,y: x+y, successesCount)

for i in range(n+1):
    xSuperiorOrEqual = reduce(lambda x,y: x+y, successesCount[i:])
    asFraction = fractions.Fraction(xSuperiorOrEqual, leaves)
    print('P( X >=',i,') :', str(asFraction) + ' ( '+str(xSuperiorOrEqual)+'/' + str(leaves) +' )' if asFraction > 0 else probXSuperiorOrEqual)