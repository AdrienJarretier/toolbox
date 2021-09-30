from collections.abc import Iterable
import numpy as np


class Point(Iterable):

    def distanceMatrix(points):

        matrix = np.zeros((len(points), len(points)))

        for i in range(len(points)):
            for j in range(len(points)):
                matrix[i][j] = points[i].distance(points[j])

        return matrix

    def __init__(self, x, y, labelText=''):
        self.x = x
        self.y = y
        self._data = [self.x, self.y]
        self.label = {'text': labelText, 'color': 'white'}

    def __iter__(self):
        return self._data.__iter__()

    def setLabel(self, label, color=None):
        self.label['text'] = label
        if color is not None:
            self.label['color'] = color

    def getLabel(self):
        return self.label['text']

    def getLabelColor(self):
        return self.label['color']

    def distance(self, otherPoint):
        return ((self.x-otherPoint.x)**2+(self.y-otherPoint.y)**2)**0.5
