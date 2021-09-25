import random
import math
import matplotlib.image as mpimg
import string

import numpy as np

from Point import Point
from plot import *

# SEED = random.randrange(2**64)
SEED = 13424815307631118833
print('seed :', SEED)
random.seed(SEED)

img = mpimg.imread('test_image.jpg')


RADIUS = max(img.shape[0], img.shape[1])/2

points = []


def pickPoint():

    pickedAngle = random.uniform(0, 2*math.pi)
    pickedRadius = random.uniform(0, RADIUS**2)

    x = math.sqrt(pickedRadius)*math.cos(pickedAngle)
    y = math.sqrt(pickedRadius)*math.sin(pickedAngle)

    return (x, y)


def sortByDistanceFromCenter(points):
    points.sort(key=lambda p: math.sqrt(p.x**2+p.y**2))


def argmin(list, key):
    index_min = 0
    val_min = key(list[index_min])
    for i in range(len(list)):
        e = list[i]
        if key(e) < val_min:
            val_min = key(e)
            index_min = i

    return index_min


def tspNearestNeighbour(points, distanceMatrix=None):

    if distanceMatrix is None:
        # first point is the center of the disk
        distMat = Point.distanceMatrix([Point(0, 0)] + points)
    else:
        distMat = np.copy(distanceMatrix)

    print(distMat)

    def compare(col):
        return lambda line: line[col] if line[col] > 0 else np.Inf


    index_min = argmin(distMat, compare(0))
    print()
    print(index_min)
    print(distMat[index_min])

    # orderedPoints = []
    # currentPoint = 

    # while len(distMat) > 0:
 
    #     index_min = argmin(distMat, compare(2))




for i in range(4):

    x, y = pickPoint()
    p = Point(x, y, string.ascii_uppercase[i])
    points.append(p)

tspNearestNeighbour(points)

# plotPoints(points, RADIUS, color=[[1, 0, 0, 1/2]], backgroundImage=img)
