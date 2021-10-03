import PySimpleGUI as sg
import random

SEED = random.randrange(2**64)
# SEED = 10487079130662621353
print('seed :', SEED)
random.seed(SEED)

CANVAS_SIZE = (random.randint(200, 500), random.randint(200, 500))
# CANVAS_SIZE = (200, 200)
BOTTOM_LEFT = (-CANVAS_SIZE[0]/2, -CANVAS_SIZE[1]/2)
TOP_RIGHT = (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2)

print('CANVAS_SIZE :', CANVAS_SIZE)
print('BOTTOM_LEFT :', BOTTOM_LEFT)
print('TOP_RIGHT :', TOP_RIGHT)

graphicalArea = sg.Graph(CANVAS_SIZE, BOTTOM_LEFT, TOP_RIGHT)

layout = [[
    graphicalArea
]]

window = sg.Window('Draw Circle', layout, element_padding=(8, 8), font=("default", 14), no_titlebar=False,
                   grab_anywhere=False, use_custom_titlebar=True, titlebar_icon="", enable_close_attempted_event=True)

window.finalize()


def drawGrid(cellSize):
    cellWidth = cellSize[0]
    cellHeight = cellSize[1]
    lines = int(CANVAS_SIZE[1]/cellHeight)+1
    cols = int(CANVAS_SIZE[0]/cellWidth)+1

    # graphicalArea.draw_line(
    #     (BOTTOM_LEFT[0], BOTTOM_LEFT[1]+1),
    #     (TOP_RIGHT[0], BOTTOM_LEFT[1]+1))

    y = BOTTOM_LEFT[1]+1
    print('y :', y)
    graphicalArea.draw_line((BOTTOM_LEFT[0], y), (TOP_RIGHT[0], y))
    for i in range(1, lines+1):
        y = i*cellHeight+BOTTOM_LEFT[1]
        print('y :', y)
        graphicalArea.draw_line((BOTTOM_LEFT[0], y), (TOP_RIGHT[0], y))

    for j in range(cols-1):
        x = j*cellWidth+BOTTOM_LEFT[0]
        # print('x :', x)
        graphicalArea.draw_line((x, TOP_RIGHT[1]), (x, BOTTOM_LEFT[1]))
    x = (cols-1)*cellWidth+BOTTOM_LEFT[0]-1
    # print('x :', x)
    graphicalArea.draw_line(
        (x, TOP_RIGHT[1]),
        (x, BOTTOM_LEFT[1]))


# CELLS_SIZE = (CANVAS_SIZE[0]/random.randint(1, 20), CANVAS_SIZE[1]/random.randint(1, 20))
CELLS_SIZE = (random.randint(10, 100), random.randint(10, 100))
# CELLS_SIZE = (50, 50)
print('CELLS_SIZE :', CELLS_SIZE)
drawGrid(CELLS_SIZE)


circleId = graphicalArea.draw_circle(
    (0, 0), 50, line_color='black', line_width=4)

print('circle id :', circleId)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()
