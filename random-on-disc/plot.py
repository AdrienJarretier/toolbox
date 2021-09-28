import matplotlib.pyplot as plt
from Point import Point


class Plot:

    def __init__(self):
        pass

    def plotPoints(self, points: list[Point], radius=1.0, color=[[0, 0, 0, 1/5]], backgroundImage=None):

        transposedPoints = list(map(list, zip(*points)))

        fig = plt.figure(1, [7.2, 7.2])

        if backgroundImage is not None:
            w = backgroundImage.shape[0]
            h = backgroundImage.shape[1]
            plt.imshow(backgroundImage, extent=[-w/2, w/2, h/2, -h/2])

        circle = plt.Circle((0, 0), radius, fill=False, color='red')
        ax = fig.gca()
        ax.add_patch(circle)
        plt.scatter(transposedPoints[0], transposedPoints[1], c=color)

        for point in points:
            plt.annotate(point.label,  # this is the text
                         point._data, color='white')

    def linkPoints(self, points):

        for i in range(len(points)-1):
            plt.plot([points[i].x, points[i+1].x],
                     [points[i].y, points[i+1].y])

    def show(self):

        plt.show()
