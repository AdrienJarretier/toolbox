from collections.abc import Iterable
import numpy as np

class Point(Iterable):

    def distanceMatrix(points):

        matrix = np.zeros((len(points), len(points)))

        for i in range(len(points)):
            for j in range(len(points)):
                matrix[i][j] = points[i].distance(points[j])

        return matrix

    def __init__(self, x, y, label=''):
        self.x = x
        self.y = y
        self._data = [self.x, self.y]
        self.label = label

    def __iter__(self):
        return self._data.__iter__()

    def setLabel(self, label):
        self.label = label

    def distance(self, otherPoint):
        return ((self.x-otherPoint.x)**2+(self.y-otherPoint.y)**2)**0.5
