import PySimpleGUI as sg

CANVAS_SIZE = (200, 200)
BOTTOM_LEFT = (-CANVAS_SIZE[0]/2, -CANVAS_SIZE[1]/2)
TOP_RIGHT = (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2)

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
    lines = int((TOP_RIGHT[1]-BOTTOM_LEFT[1])/cellHeight)
    cols = int((TOP_RIGHT[0]-BOTTOM_LEFT[0])/cellWidth)

    for i in range(lines):
        y = i*cellHeight+BOTTOM_LEFT[1]
        print('y :', y)
        graphicalArea.draw_line((BOTTOM_LEFT[0], y+1), (TOP_RIGHT[0], y+1))

    for j in range(cols):
        x = j*cellWidth+BOTTOM_LEFT[0]
        print('x :', x)
        graphicalArea.draw_line((x, TOP_RIGHT[1]), (x, BOTTOM_LEFT[1]))


drawGrid((20, 20))


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
