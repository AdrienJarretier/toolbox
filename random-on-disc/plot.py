import matplotlib.pyplot as plt
from Point import Point


def plotPoints(points: list[Point], color=[[0, 0, 0, 1/5]]):
    transposedPoints = list(map(list, zip(*points)))

    plt.figure(1, [7.2,7.2])
    plt.scatter(transposedPoints[0], transposedPoints[1], c=color)
    plt.show()
