from collections.abc import Iterable


class Point(Iterable):

    def __init__(self, x, y, label=''):
        self._data = [x, y]
        self.label = label

    def __iter__(self):
        return self._data.__iter__()
