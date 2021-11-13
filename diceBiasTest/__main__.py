from scipy.stats import chisquare
import pandas as pd
from contextlib import redirect_stdout
import pathlib

for obsContent in pathlib.Path('observations').iterdir():

    if obsContent.is_dir():

        diceDirPath = obsContent

        DIE_SIDES = int(diceDirPath.name[1:])

        observed = [0]*DIE_SIDES

        for obsValuesPath in diceDirPath.iterdir():

            with open(obsValuesPath) as values:
                for v in values:
                    observed[int(v)-1] += 1

            expected = [sum(observed)/DIE_SIDES] * DIE_SIDES

            chisq, p = chisquare(observed, expected)

            print('\n')

            for _ in range(2):
                outputFolderPath = pathlib.Path('testsResults', diceDirPath.name)
                try:
                    outputResultsPath = outputFolderPath.joinpath(obsValuesPath.name)
                    with open(outputResultsPath, 'w') as resultsFile:
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

                        print('tests results in : ', outputResultsPath)
                except FileNotFoundError:
                    outputFolderPath.mkdir(parents=True)
                else:
                    break
