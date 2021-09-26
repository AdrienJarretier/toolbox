
import math
import random

# SEED = random.randrange(2**64)
SEED = 9695349962937902509
print('seed :', SEED)
random.seed(SEED)


def randomPoint(diskRadius):

    pickedAngle = random.uniform(0, 2*math.pi)
    pickedRadius = random.uniform(0, diskRadius**2)

    x = math.sqrt(pickedRadius)*math.cos(pickedAngle)
    y = math.sqrt(pickedRadius)*math.sin(pickedAngle)

    return (x, y)
