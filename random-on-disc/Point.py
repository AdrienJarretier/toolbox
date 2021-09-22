from collections.abc import Iterable

class Point(Iterable):

    def __init__(self, x, y):
        self._data = [x,y]

    def __iter__(self):
        return self._data.__iter__()
