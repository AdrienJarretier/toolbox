import random
import fractions


conditions = 2

replicates = 6

simulationsCount = 60000


samples = conditions*replicates


orderedLabels = list(range(conditions))*replicates

successesPerExp = {}

for i in range(0, replicates*conditions+1):
    successesPerExp[i] = 0

for _ in range(simulationsCount):

    for _ in range(replicates):
        randomDraw = orderedLabels.copy()

        random.shuffle(randomDraw)

        successes = 0
        for i in range(len(orderedLabels)):

            if randomDraw[i] == orderedLabels[i]:
                successes += 1

    successesPerExp[successes] += 1


for i in range(len(successesPerExp)):
    successesPerExp[i] /= simulationsCount


for i in range(1, len(successesPerExp)):
    successesPerExp[i] += successesPerExp[i-1]


for i in range(len(successesPerExp)):

    if successesPerExp[i] > 0:
        print(i, ':', successesPerExp[i])