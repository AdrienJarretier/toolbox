
import math
import random

def randomPoint(diskRadius):

    pickedAngle = random.uniform(0, 2*math.pi)
    pickedRadius = random.uniform(0, diskRadius**2)

    x = math.sqrt(pickedRadius)*math.cos(pickedAngle)
    y = math.sqrt(pickedRadius)*math.sin(pickedAngle)

    return (x, y)
