import copy
from collections.abc import MutableMapping

RESOURCES = ['machineParts', 'electronics']


class Stock(MutableMapping):

    def __init__(self, initializer):
        self._stock = {}

        for resource in RESOURCES:
            if initializer[resource]:
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


currentStock = Stock({
    "machineParts": 8,
    "electronics": 2
})

consumption = Stock({
    "machineParts": 0.6,
    "electronics": 0.5
})


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

# supplies =

for i in range(2):
    expectedStock = getExpectedStock(newStock)
    maxMissing = getMaxMissing(expectedStock)
    newStock[maxMissing['resource']] += 5
    print('max missing :', maxMissing)
    printStocks(newStock)
