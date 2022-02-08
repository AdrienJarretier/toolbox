from plotnine import ggplot, geom_col, aes, geom_text, position_stack, position_nudge, scale_x_continuous, scale_x_discrete
import random
import numpy as np
import pandas as pd

conditions = 2

replicates = 6

simulationsCount = 100000


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

# print(successesPerExp)

for i in range(len(successesPerExp)):
    if successesPerExp[i] == 0:
        del successesPerExp[i]

print(successesPerExp)

values = list(successesPerExp.values())
flipped = np.flip(values)
flippedCumulatedValues = np.cumsum(flipped)
cumulatedValues = np.flip(flippedCumulatedValues)
cumulatedPercentages = list(map(lambda x: x/simulationsCount, cumulatedValues))


print('values: ', values)
print('flipped: ', flipped)
print('flippedCumulatedValues: ', flippedCumulatedValues)
print('cumulatedValues: ', cumulatedValues)
print('cumulatedPercentages: ', cumulatedPercentages)

successesPerExp.update(zip(successesPerExp, cumulatedPercentages))

print()
for i in successesPerExp.keys():
    print(i, ':', successesPerExp[i])

decimalsForRound = 0
lastValue = list(successesPerExp.values())[-1]
while int(lastValue * 10**decimalsForRound) == 0:
    decimalsForRound += 1

data = pd.DataFrame(data={"x": successesPerExp.keys(),
                    "y": successesPerExp.values()})


plot = (ggplot(data,
               aes(x="x", y="y", label='y')
               )
        + geom_col()
        + geom_text(data=data.round(decimalsForRound),
                    position=position_nudge(y=0.03))
        + scale_x_continuous(breaks=list(successesPerExp.keys()))
        )


print(plot)
