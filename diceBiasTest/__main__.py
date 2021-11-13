from scipy.stats import chisquare
import pandas as pd
from contextlib import redirect_stdout
import pathlib

DIE_SIDES = 20

observed = [0]*DIE_SIDES

with open('observations/d20/values.txt') as values:
    for v in values:
        observed[int(v)-1] += 1


expected = [sum(observed)/DIE_SIDES] * DIE_SIDES

chisq, p = chisquare(observed, expected)

for _ in range(2):
    outputFolderPath = pathlib.Path('testsResults', 'dice')
    try:
        with open('testsResults/dice/filename.txt', 'w') as resultsFile:
            with redirect_stdout(resultsFile):
                print()

                print('********************* d' +
                      str(DIE_SIDES), '*********************')

                print(pd.DataFrame([expected, observed], ['expected', 'observed'], [
                    i for i in range(1, len(observed)+1)]))
                print('\n')

                print('======= chi-squared test statistic =======')
                print(chisq)
                print('\n')
                print('======= p-value =======')
                print(p, end='')
                if p < 0.05:
                    print(' *', end='')
                    if p < 0.01:
                        print('*', end='')
                        if p < 0.001:
                            print('*', end='')
                print('\n')
    except FileNotFoundError:
        outputFolderPath.mkdir(parents=True)
    else:
        break
