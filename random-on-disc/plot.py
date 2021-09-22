import matplotlib.pyplot as plt
from Point import Point


def plotPoints(points: list[Point]):
    transposedPoints = list(map(list, zip(*points)))

    plt.scatter(transposedPoints[0], transposedPoints[1], c=[[0, 0, 0, 1/5]])
    plt.show()
