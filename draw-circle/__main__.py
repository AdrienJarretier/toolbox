import PySimpleGUI as sg

CANVAS_SIZE = (200, 200)
BOTTOM_LEFT = (-CANVAS_SIZE[0]/2, -CANVAS_SIZE[1]/2)
TOP_RIGHT = (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2)

DEFAULT_GRID_RESOLUTION = 1

print('CANVAS_SIZE :', CANVAS_SIZE)
print('BOTTOM_LEFT :', BOTTOM_LEFT)
print('TOP_RIGHT :', TOP_RIGHT)

graphicalArea = sg.Graph(CANVAS_SIZE, BOTTOM_LEFT, TOP_RIGHT)


def drawGrid(cellSize):
    cellWidth = cellSize[0]
    cellHeight = cellSize[1]
    lines = int(CANVAS_SIZE[1]/cellHeight)+1
    cols = int(CANVAS_SIZE[0]/cellWidth)+1

    y = BOTTOM_LEFT[1]+1
    # print('y :', y)
    graphicalArea.draw_line((BOTTOM_LEFT[0], y), (TOP_RIGHT[0], y))
    for i in range(1, lines+1):
        y = i*cellHeight+BOTTOM_LEFT[1]
        # print('y :', y)
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


###################### gridResolution ######################
gridResolutionInput = sg.Input(
    1, (3, None), key='-GRID_RESOLUTION-')
###################### -------------- ######################


layout = [[graphicalArea, sg.Text(
    'grid resolution :'), gridResolutionInput]]

window = sg.Window('Draw Circle', layout, element_padding=(8, 8), font=("default", 14), no_titlebar=False,
                   grab_anywhere=False, use_custom_titlebar=True, titlebar_icon="", enable_close_attempted_event=True,
                   return_keyboard_events=True)

window.finalize()


gridCellsSize = (CANVAS_SIZE[0]/DEFAULT_GRID_RESOLUTION,
                 CANVAS_SIZE[1]/DEFAULT_GRID_RESOLUTION)
print('CELLS_SIZE :', gridCellsSize)
drawGrid(gridCellsSize)

circleId = graphicalArea.draw_circle(
    (0, 0), 50, line_color='black', line_width=4)

print('circle id :', circleId)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    # print(values)
    # print(type(event))

    ###################### get inputs values ######################

    gridResolution = int(values['-GRID_RESOLUTION-'])

    ###################### ----------------- ######################

    if window.find_element_with_focus() == gridResolutionInput:
        if event == 'Up:38':
            gridResolution += 1
        if event == 'Down:40' and gridResolution > 1:
            gridResolution -= 1
        gridResolutionInput.update(gridResolution)

    print(gridResolution)

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()
