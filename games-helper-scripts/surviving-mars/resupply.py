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


totalStock = 0
tmpConsumptionParts = 0

expectedStock = {}

for resource in currentStock:
    totalStock += currentStock[resource]
    tmpConsumptionParts += consumption[resource]

tmpStockPerPart = totalStock/tmpConsumptionParts

for resource in currentStock:

    expectedStock[resource] = tmpStockPerPart * consumption[resource]

newStock = copy.deepcopy(currentStock)

newStock['electronics'] += 5

print('expected ', expectedStock)
print('new stock', newStock)

for resource in expectedStock:
    print(resource, newStock[resource]-expectedStock[resource])
