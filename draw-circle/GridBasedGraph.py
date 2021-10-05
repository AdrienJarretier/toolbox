import random
from PySimpleGUI import Graph


class GridBasedGraph(Graph):

    def __init__(self, gridSize, cellSize, key=None):
        self.gridSize = gridSize
        self.cellSize = cellSize
        CANVAS_SIZE = self.getTotalSize()
        self.BOTTOM_LEFT = (-CANVAS_SIZE[0]/2, -CANVAS_SIZE[1]/2)
        self.TOP_RIGHT = (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2)
        super().__init__(CANVAS_SIZE, self.BOTTOM_LEFT,
                         self.TOP_RIGHT, enable_events=True, key=key)

    def getTotalSize(self):
        return (self.gridSize[0]*self.cellSize, self.gridSize[1]*self.cellSize)

    def drawGrid(self):
        lines = self.gridSize[1]+1
        cols = self.gridSize[0]+1

        y = self.BOTTOM_LEFT[1]+1
        # print('y :', y)
        self.draw_line((self.BOTTOM_LEFT[0], y), (self.TOP_RIGHT[0], y))
        for i in range(1, lines+1):
            y = i*self.cellSize+self.BOTTOM_LEFT[1]
            # print('y :', y)
            self.draw_line((self.BOTTOM_LEFT[0], y), (self.TOP_RIGHT[0], y))

        for j in range(cols-1):
            x = j*self.cellSize+self.BOTTOM_LEFT[0]
            # print('x :', x)
            self.draw_line((x, self.TOP_RIGHT[1]), (x, self.BOTTOM_LEFT[1]))
        x = (cols-1)*self.cellSize+self.BOTTOM_LEFT[0]-1
        # print('x :', x)
        self.draw_line(
            (x, self.TOP_RIGHT[1]),
            (x, self.BOTTOM_LEFT[1]))

    def draw_circle(self, center_location, radius, fill_color=None, line_color='black', line_width=1):
        center_location = (
            center_location[0]*self.cellSize, center_location[1]*self.cellSize)
        super().draw_circle(center_location, radius *
                            self.cellSize, fill_color, line_color, line_width)

    def mapPixelToCoords(self, point):
        return tuple([c / self.cellSize for c in point])

    def mapCoordsToPixels(self, point):
        return tuple([c * self.cellSize for c in point])

    # round point components so that it snaps to the grid
    def snapToGrid(self, point):
        def roundToHalf(x):
            roundedDecimal = 0
            decimal = abs(x) % 1
            if 0.25 <= decimal and decimal < 0.75:
                roundedDecimal = 0.5
            elif decimal >= 0.75:
                roundedDecimal = 1

            if x >= 0:
                return int(x) + roundedDecimal
            else:
                return int(x) - roundedDecimal

        return tuple([roundToHalf(c) for c in point])


# testGraph = GridBasedGraph((5, 5), 30)

# for _ in range(5):
#     point = (random.uniform(-1, 1),random.uniform(-1, 1))
#     print(point, testGraph.snapToGrid(point))

# print(testGraph.mapPixelToCoords((30, 3)))
# print(testGraph.mapCoordsToPixels((1, 0.1)))
