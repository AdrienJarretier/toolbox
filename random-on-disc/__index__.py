
from bb import bnbSolve
from randomOnDisk import randomPoint
from tsp import orderPoints, tspNearestNeighbour, routeLength
import matplotlib.image as mpimg
import string

from Point import Point
from plot import Plot

img = mpimg.imread('test_image.jpg')


RADIUS = max(img.shape[0], img.shape[1])/2

POINTS_COUNT = 1

points = []


print('picking random points...')
for i in range(POINTS_COUNT):

    x, y = randomPoint(RADIUS)
    p = Point(x, y, string.ascii_uppercase[i % 26])
    points.append(p)


def labelAddOrder(points):
    for i in range(len(points)):
        point = points[i]
        point.setLabel(point.label + str(i+1))


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

    return orderedPoints


def plotAll(points):
    plot = Plot()
    plot.plotPoints(points, RADIUS, color=[
        [1, 0, 0, 1/2]], backgroundImage=img)
    plot.linkPoints(points + [points[0]])
    plot.show()


# solvedPoints = greedySolve([Point(0, 0)]+points)
solvedPoints = bnbSolve(points)
print('route length:', routeLength(solvedPoints))

labelAddOrder(solvedPoints)
# plotAll(solvedPoints)

