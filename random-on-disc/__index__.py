import random
import math
import matplotlib.image as mpimg

from Point import Point
from plot import *


img = mpimg.imread('test_image.jpg')

RADIUS = max(img.shape[0], img.shape[1])/2

points = []


def pickPoint():

    pickedAngle = random.uniform(0, 2*math.pi)
    pickedRadius = random.uniform(0, RADIUS**2)

    x = math.sqrt(pickedRadius)*math.cos(pickedAngle)+RADIUS
    y = math.sqrt(pickedRadius)*math.sin(pickedAngle)+RADIUS

    return Point(x, y)


for i in range(10):

    points.append(pickPoint())

plotPoints(points, RADIUS, color=[[1, 0, 0, 1/2]], backgroundImage=img)
