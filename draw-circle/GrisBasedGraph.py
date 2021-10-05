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
        return (self.gridSize[0]*self.cellSize[0], self.gridSize[1]*self.cellSize[1])

    def drawGrid(self):
        cellWidth = self.cellSize[0]
        cellHeight = self.cellSize[1]
        lines = self.gridSize[1]+1
        cols = self.gridSize[0]+1

        y = self.BOTTOM_LEFT[1]+1
        # print('y :', y)
        self.draw_line((self.BOTTOM_LEFT[0], y), (self.TOP_RIGHT[0], y))
        for i in range(1, lines+1):
            y = i*cellHeight+self.BOTTOM_LEFT[1]
            # print('y :', y)
            self.draw_line((self.BOTTOM_LEFT[0], y), (self.TOP_RIGHT[0], y))

        for j in range(cols-1):
            x = j*cellWidth+self.BOTTOM_LEFT[0]
            # print('x :', x)
            self.draw_line((x, self.TOP_RIGHT[1]), (x, self.BOTTOM_LEFT[1]))
        x = (cols-1)*cellWidth+self.BOTTOM_LEFT[0]-1
        # print('x :', x)
        self.draw_line(
            (x, self.TOP_RIGHT[1]),
            (x, self.BOTTOM_LEFT[1]))
