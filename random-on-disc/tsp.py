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
        # first point is the center of the disk
        distMat = Point.distanceMatrix([Point(0, 0)] + points)
    else:
        distMat = np.copy(distanceMatrix)

    def compare(col):
        return lambda line: line[col] if line[col] > 0 else np.Inf

    index_min = argmin(distMat, compare(0))

    orderedPointsIndices = [0]

    while len(orderedPointsIndices) < len(points)+1:

        index_min = argmin(distMat, compare(
            orderedPointsIndices[-1]), orderedPointsIndices)
        orderedPointsIndices.append(index_min)

    return orderedPointsIndices[1:]


def routeLength(points):
    diskCenter = Point(0, 0)
    length = diskCenter.distance(points[0])
    for i in range(1, len(points)):
        length += points[i-1].distance(points[i])

    length += points[-1].distance(diskCenter)

    return length
