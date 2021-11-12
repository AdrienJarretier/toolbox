from scipy.stats import chisquare
import numpy as np
import pandas as pd

DIE_SIDES = 20

observed = [0]*DIE_SIDES

with open('values.txt') as values:
    for v in values:
        observed[int(v)-1] += 1


expected = [sum(observed)/DIE_SIDES] * DIE_SIDES

chisq, p = chisquare(observed, expected)


print()

print('********************* d' + str(DIE_SIDES), '*********************')

print(pd.DataFrame([expected, observed], ['expected', 'observed'], [i for i in range(1, len(observed)+1)]))
print('\n')

print('======= chi-squared test statistic =======')
print(chisq)
print('\n')
print('======= p-value =======')
print(p)
print('\n')
