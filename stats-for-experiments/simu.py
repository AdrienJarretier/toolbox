import random
import numpy as np
from plotnine import ggplot, geom_col, aes, geom_text, position_stack, position_nudge
import pandas as pd

conditions = 2

replicates = 1

simulationsCount = 30000


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


plot = (ggplot(pd.DataFrame(data={"x": successesPerExp.keys(), "y": successesPerExp.values()}),
               aes(x="x", y="y", label='y')
               )
        + geom_col()
        + geom_text(position=position_nudge(y=0.03))
        )


# data = pd.DataFrame(successesPerExp.items(), columns=['age', 'pop'])

# plot = ggplot(pd.DataFrame(data), aes("age")
#               ) + geom_col(aes(y='pop'))

print(plot)
