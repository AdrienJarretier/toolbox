from PySimpleGUI import Graph


class GrisBasedGraph(Graph):

    def __init__(self, gridSize, cellSize):
        self.gridSize = gridSize
        self.cellSize = cellSize
        CANVAS_SIZE = self.getTotalSize()
        self.BOTTOM_LEFT = (-CANVAS_SIZE[0]/2, -CANVAS_SIZE[1]/2)
        self.TOP_RIGHT = (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2)
        super().__init__(CANVAS_SIZE, self.BOTTOM_LEFT, self.TOP_RIGHT)

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
