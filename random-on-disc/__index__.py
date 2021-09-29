
from plot import Plot
from Point import Point
from bb import bnbSolve
from randomOnDisk import randomPoint
from tsp import orderPoints, tspNearestNeighbour, routeLength
import matplotlib.image as mpimg
import string
import random

SEED = random.randrange(2**64)
# SEED = 9695349962937902509
print('seed :', SEED)
random.seed(SEED)


img = mpimg.imread('test_image.jpg')


DISTRIB_RAIDUS_CAP = 0.3


RADIUS = max(img.shape[0], img.shape[1])/2

POINTS_COUNT = 7

points = []


print('picking random points...')
for i in range(POINTS_COUNT):

    x, y = randomPoint(RADIUS)
    p = Point(x, y, string.ascii_uppercase[i % 26])
    points.append(p)


def labelAddOrder(points):
    for i in range(1, len(points)-1):
        point = points[i]
        point.setLabel(point.label + str(i))


def greedySolve(points):
    points = points
    print('solving tsp...')
    orderedPointsIndices = tspNearestNeighbour(points)
    print('tsp solved')
    print(orderedPointsIndices)
    print(points)

    orderedPoints = orderPoints(orderedPointsIndices, points)

    print('plotting points')
    print('greedy path :', [p.label for p in orderedPoints])

    return orderedPoints + [points[0]]


def plotAll(points):
    plot = Plot()
    plot.plotPoints(points, RADIUS, color=[
        [1, 0, 0, 1/2]], backgroundImage=img)
    plot.linkPoints(points)
    plot.show()


# solvedPoints = greedySolve([Point(0, 0)]+points)
solvedPoints = bnbSolve(points)
print('route length:', routeLength(solvedPoints))

labelAddOrder(solvedPoints)
plotAll(solvedPoints)
