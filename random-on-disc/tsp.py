import numpy as np

from Point import Point


def argmin(list, key, excluded=[]):
    excluded = excluded.copy()

    index_min = None
    val_min = np.Inf
    for i in range(len(list)):
        # if i in excluded : remove i from excluded and continue to next iteration
        try:
            exc_index = excluded.index(i)
            excluded.pop(exc_index)
        # if i not in excluded, compare list[i] to val_min
        except:
            e = list[i]
            if key(e) < val_min:
                val_min = key(e)
                index_min = i

    return index_min

# def sortByDistanceFromCenter(points):
#     points.sort(key=lambda p: math.sqrt(p.x**2+p.y**2))


def tspNearestNeighbour(points, distanceMatrix=None):

    if distanceMatrix is None:
        distMat = Point.distanceMatrix(points)
    else:
        distMat = np.copy(distanceMatrix)

    def compare(col):
        return lambda line: line[col] if line[col] > 0 else np.Inf

    index_min = argmin(distMat, compare(0))

    orderedPointsIndices = [0]

    while len(orderedPointsIndices) < len(points):

        index_min = argmin(distMat, compare(
            orderedPointsIndices[-1]), orderedPointsIndices)
        orderedPointsIndices.append(index_min)

    return orderedPointsIndices


def routeLength(points):

    if len(points) == 0:
        return 0

    # diskCenter = Point(0, 0)
    # length = diskCenter.distance(points[0])

    length = 0
    for i in range(1, len(points)):
        length += points[i-1].distance(points[i])

    # length += points[-1].distance(diskCenter)

    return length


def orderPoints(orderedIndices, points):
    orderedPoints = []
    for i in range(len(orderedIndices)):
        orderedPointIndex = orderedIndices[i]
        point = points[orderedPointIndex]
        orderedPoints.append(point)

    return orderedPoints

