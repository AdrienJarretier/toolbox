import copy


# returns a list of size n averaged data from originalData
def averageToNPoints(originalData, n):
    offset = 0
    originalDataLen = len(originalData)

    if n >= originalDataLen:
        return copy.copy(originalData)

    originalDataLen -= originalDataLen % n

    avgWindowSize = int(originalDataLen/n)

    averagedData = []

    while len(averagedData) < n:
        sum = 0
        for i in range(avgWindowSize):
            sum += originalData[offset+i]

        averagedData.append(sum/avgWindowSize)
        offset += avgWindowSize

    return averagedData


# for n in range(1, 5):
#     print()
#     print('n :', n)
#     for length in range(20):
#         print()
#         print('length :', length)
#         data = [i for i in range(length)]
#         print(data)
#         print(averageToNPoints(data, n))
