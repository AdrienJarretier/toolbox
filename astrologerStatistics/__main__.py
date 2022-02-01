from scipy.special import binom
import fractions
from functools import reduce

def pSuccess(x, p, n):

    return binom(n,x)*p**x*(1-p)**(n-x)



p = 1/12
n = 12

probSuccesses = []

for x in range(n+1):

    print('x :', x)
    print('p :', p)
    print('n :', n)
    probabilitySuccess = pSuccess(x,p,n)
    probSuccesses.append(probabilitySuccess)
    print(probabilitySuccess)
    print(fractions.Fraction(probabilitySuccess).limit_denominator(100))
    print('------------')


for i in range(n+1):
    probXSuperiorOrEqual = reduce(lambda x,y: x+y, probSuccesses[i:])
    asFraction = fractions.Fraction(probXSuperiorOrEqual).limit_denominator(100)
    print('P( X >=',i,') :', str(asFraction) + ' ( '+str(probXSuperiorOrEqual)+' )' if asFraction > 0 else probXSuperiorOrEqual)