
from randomOnDisk import randomPoint
from tsp import tspNearestNeighbour, routeLength
import matplotlib.image as mpimg
import string

from Point import Point
from plot import *

img = mpimg.imread('test_image.jpg')


RADIUS = max(img.shape[0], img.shape[1])/2

points = []


print('picking random points...')
for i in range(5):

    x, y = randomPoint(RADIUS)
    p = Point(x, y, string.ascii_uppercase[i%26])
    points.append(p)


print('solving tsp...')
orderedPointsIndices = tspNearestNeighbour(points)
print('tsp solved')

orderedPoints = []
for i in range(len(orderedPointsIndices)):
    orderedPointIndex = orderedPointsIndices[i]
    point = points[orderedPointIndex-1]
    # point.setLabel('')
    point.setLabel(point.label + str(i+1))
    orderedPoints.append(point)

print('plotting points')
print('route length :', routeLength(orderedPoints))
plotPoints(orderedPoints, RADIUS, color=[[1, 0, 0, 1/2]], backgroundImage=img)

