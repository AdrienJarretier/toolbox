import matplotlib.pyplot as plt
from Point import Point


def plotPoints(points: list[Point], radius=1.0, color=[[0, 0, 0, 1/5]], backgroundImage=None):

    transposedPoints = list(map(list, zip(*points)))

    fig = plt.figure(1, [7.2, 7.2])

    if backgroundImage is not None:
        plt.imshow(backgroundImage)

    circle = plt.Circle((radius, radius), radius, fill=False, color='red')
    ax = fig.gca()
    ax.add_patch(circle)
    plt.scatter(transposedPoints[0], transposedPoints[1], c=color)

    for point in points:
        plt.annotate(point.label,  # this is the text
                     point._data)

    plt.show()
