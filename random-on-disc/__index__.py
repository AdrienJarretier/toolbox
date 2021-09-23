import random
import math
import matplotlib.image as mpimg

from Point import Point
from plot import *

# SEED = random.randrange(2**64)
SEED = 3205471914082095861
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


for i in range(20):

    x, y = pickPoint()
    p = Point(x, y, i+1)
    points.append(p)


sortByDistanceFromCenter(points)

for i in range(len(points)):
    points[i].setLabel(i+1)

plotPoints(points, RADIUS, color=[[1, 0, 0, 1/2]], backgroundImage=img)
