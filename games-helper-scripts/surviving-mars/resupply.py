import copy

currentStock = {
    "machineParts": 8,
    "electronics": 2
}

consumption = {
    "machineParts": 0.6,
    "electronics": 0.5
}


# def resupply(machineParts, electronics):
#     newStock = {
#         "machineParts": currentStock["machineParts"]+machineParts,
#         "electronics": currentStock["electronics"]+electronics
#     }

#     newStock["machineParts"]

#     return abs(1.2-(m+mx)/(e+ex))


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
    print('stock    ', stock)
    print()


printStocks(currentStock)


def incSupplies():

    expectedStock = getExpectedStock(newStock)

    maxMissing = 0
    resourceToInc = None
    for resource in expectedStock:
        print(resource, newStock[resource]-expectedStock[resource])

        missing = expectedStock[resource]-newStock[resource]
        if missing > maxMissing:
            maxMissing = missing
            resourceToInc = resource

    newStock[resourceToInc] += 5

    printStocks(newStock)


incSupplies()
