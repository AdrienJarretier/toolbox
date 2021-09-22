import random
import math

from Point import Point
from plot import *

RADIUS = 10

points = []


def pickPoint():

    pickedAngle = random.uniform(0, 2*math.pi)
    pickedRadius = random.uniform(0, RADIUS**2)

    x = math.sqrt(pickedRadius)*math.cos(pickedAngle)
    y = math.sqrt(pickedRadius)*math.sin(pickedAngle)

    return Point(x, y)


for i in range(2000):

    points.append(pickPoint())

plotPoints(points, RADIUS, color=[[0, 0, 0, 1/4]])
