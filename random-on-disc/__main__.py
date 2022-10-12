
from plot import Plot
from Point import Point
from bb import bnbSolve
from randomOnDisk import randomPoint
from tsp import orderPoints, tspNearestNeighbour, routeLength
import matplotlib.image as mpimg
import string
import random


POINTS_COUNT = 7

# SEED = 8126021129041542390
# EXCLUDED_LABELS = ['A', 'E', 'G', 'D']

try:
    random.seed(SEED)
except:
    SEED = random.randrange(2**64)
    random.seed(SEED)


img = mpimg.imread('test_images/20220714010910_1.jpg')
# img = None

DISTRIB_RAIDUS_CAP = 0.3

RATIO_DISTRIB_AREA_TOTAL_AREA = 1

if img is not None:
    TOTAL_CIRCLE_RADIUS = max(img.shape[0], img.shape[1])/2
else:
    TOTAL_CIRCLE_RADIUS = 400

points = []


RADIUS = TOTAL_CIRCLE_RADIUS * (RATIO_DISTRIB_AREA_TOTAL_AREA**0.5)


print('picking random points...')
for i in range(POINTS_COUNT):

    x, y = randomPoint(RADIUS)
    p = Point(x, y, string.ascii_uppercase[i % 26])
    points.append(p)


def labelAddOrder(points):
    for i in range(1, len(points)-1):
        point = points[i]
        point.setLabel(point.getLabel() + str(i), 'black')


def greedySolve(points):
    points = points
    print('solving tsp...')
    orderedPointsIndices = tspNearestNeighbour(points)
    print('tsp solved')
    print(orderedPointsIndices)
    print(points)

    orderedPoints = orderPoints(orderedPointsIndices, points)

    return orderedPoints + [points[0]]


def plotAll(points):
    plot = Plot()
    plot.plotPoints(points, RADIUS, color=[
        [1, 0, 0, 1/2]], backgroundImage=img)
    plot.linkPoints(points)
    plot.show()


def removeExcluded(points):
    try:
        i = 0
        while i < len(points):

            if points[i].getLabel() in EXCLUDED_LABELS:
                points.pop(i)
            else:
                i += 1
    except NameError as ne:
        print('error :', ne)
        pass


# solvedPoints = greedySolve([Point(0, 0)]+points)

removeExcluded(points)
solvedPoints = bnbSolve(points)

print('path :', [p.getLabel() for p in solvedPoints])
print('route length:', routeLength(solvedPoints))
print('seed :', SEED)

labelAddOrder(solvedPoints)
plotAll(solvedPoints)
