import copy
from collections.abc import MutableMapping

RESOURCES = ['machineParts', 'electronics']
COSTS = [90/5, 100/5]
WEIGHTS = [2000/5, 2000/5]


class Stock(MutableMapping):

    def __init__(self, initializer={}):
        self._stock = {}

        for resource in RESOURCES:
            if resource in initializer:
                self._stock[resource] = initializer[resource]
            else:
                self._stock[resource] = 0

    def __getitem__(self, key):
        return self._stock.__getitem__(key)

    def __setitem__(self, key, val):
        return self._stock.__setitem__(key, val)

    def __delitem__(self, key):
        return self._stock.__delitem__(key)

    def __iter__(self):
        return self._stock.__iter__()

    def __len__(self):
        return self._stock.__len__()

    def combine(self, otherStock):
        newStock = copy.deepcopy(self)

        for resource in RESOURCES:
            newStock[resource] += otherStock[resource]

        return newStock

    def cost(self):
        cost = 0
        for i in range(len(RESOURCES)):
            cost += self._stock[RESOURCES[i]] * COSTS[i]

        return cost

    def weight(self):
        weight = 0
        for i in range(len(RESOURCES)):
            weight += self._stock[RESOURCES[i]] * WEIGHTS[i]

        return weight


currentStock = Stock({
    "machineParts": 13,
    "electronics": 9
})

consumption = Stock({
    "machineParts": 0.2,
    "electronics": 0.2
})

MAX_COST = 23840
MAX_CARGO = 25000


newStock = copy.deepcopy(currentStock)


def getExpectedStock(stock):
    totalStock = 0
    tmpConsumptionParts = 0

    expectedStock = {}

    for resource in stock:
        totalStock += stock[resource]
        tmpConsumptionParts += consumption[resource]

    tmpStockPerPart = totalStock/tmpConsumptionParts

    for resource in stock:

        expectedStock[resource] = tmpStockPerPart * consumption[resource]

    return expectedStock


def printStocks(stock):
    print('expected ', getExpectedStock(stock))
    print('stock    ', stock._stock)
    print()


def getMaxMissing(expectedStock):
    maxMissing = {
        'qty': 0,
        'resource': None
    }

    for resource in expectedStock:

        missing = expectedStock[resource]-newStock[resource]
        if missing >= maxMissing['qty']:
            maxMissing['qty'] = missing
            maxMissing['resource'] = resource

    return maxMissing


print('initial stock :')
printStocks(currentStock)
print()

supplies = Stock()

potentialNewStocks = []

while True:
    expectedStock = getExpectedStock(newStock)
    maxMissing = getMaxMissing(expectedStock)
    potentialNewStocks.append({
        'stock': copy.deepcopy(newStock),
        'maxMissing': maxMissing,
        'supplies': copy.deepcopy(supplies)
    })

    supplies[maxMissing['resource']] += 5
    newStock = newStock.combine(supplies)

    if supplies.cost() > MAX_COST or supplies.weight() > MAX_CARGO:
        break

potentialNewStocks.sort(key=lambda s: s['maxMissing']['qty'], reverse=True)

print('potentialNewStocks:')
for s in potentialNewStocks:
    print('-'*50)
    print(
        'stock :   ', s['stock']._stock,
        '\nmissing : ', s['maxMissing'],
        '\nsupplies :', s['supplies']._stock,
        '\ncost :    ', s['supplies'].cost(),
        '\nweight :  ', s['supplies'].weight())
