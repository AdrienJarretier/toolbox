import matplotlib.pyplot as plt
from Point import Point


def plotPoints(points: list[Point], radius=1.0, color=[[0, 0, 0, 1/5]]):
    transposedPoints = list(map(list, zip(*points)))

    fig = plt.figure(1, [7.2, 7.2])
    circle = plt.Circle((0, 0), radius, fill=False)
    ax = fig.gca()
    ax.add_patch(circle)
    plt.scatter(transposedPoints[0], transposedPoints[1], c=color)
    plt.show()
