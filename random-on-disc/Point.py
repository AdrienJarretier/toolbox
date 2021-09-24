from collections.abc import Iterable


class Point(Iterable):

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
