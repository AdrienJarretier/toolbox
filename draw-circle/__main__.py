import PySimpleGUI as sg
from GridBasedGraph import GridBasedGraph

circleRadius = 4.5

graphicalArea = GridBasedGraph((32, 36), 20, key='-GRAPH_AREA-')


###################### gridResolution ######################
gridResolutionInput = sg.Input(
    1, (3, None), key='-GRID_RESOLUTION-')
###################### -------------- ######################

layout = [[sg.Column([[graphicalArea]]),
           sg.Column([[sg.Text('grid resolution :'), gridResolutionInput],
                      [sg.Button('Erase')],
                      [sg.Button('Save')]])
           ]]

window = sg.Window('Draw Circle', layout, element_padding=(8, 8), font=("default", 14), no_titlebar=False,
                   grab_anywhere=False, use_custom_titlebar=True, titlebar_icon="", enable_close_attempted_event=True,
                   return_keyboard_events=True)

window.finalize()


graphicalArea.bind("<Motion>", 'mouseMove')

graphicalArea.drawGrid()

# print('circle id :', circleId)

# Display and interact with the Window using an Event Loop
snappedCursor = None
tmpCircleAtMouse = None
while True:
    event, values = window.read()

    # print(values)
    # print('event :', event)

    ###################### get inputs values ######################

    try:
        gridResolution = int(values['-GRID_RESOLUTION-'])
    except ValueError:
        gridResolution = 0

    ###################### ----------------- ######################

    if window.find_element_with_focus() == gridResolutionInput:
        if event == 'Up:38':
            gridResolution += 1
        if event == 'Down:40' and gridResolution > 1:
            gridResolution -= 1
        gridResolutionInput.update(gridResolution)

    if event == '-GRAPH_AREA-':
        print('drawing circle at', values['-GRAPH_AREA-'])
        graphicalArea.draw_circle(
            graphicalArea.snapToGrid(
                graphicalArea.mapPixelToCoords(values['-GRAPH_AREA-'])),
            circleRadius, line_color='black', line_width=3)

    if event == '-GRAPH_AREA-mouseMove':
        # tk_canvas
        polygonCenter = graphicalArea.mapCoordsToPixels(
            graphicalArea.snapToGrid(
                graphicalArea.mapPixelToCoords(values['-GRAPH_AREA-']))
        )
        crossSize = 20
        crossPoints = [
            (polygonCenter[0]-crossSize/2, polygonCenter[1]),
            polygonCenter,
            (polygonCenter[0]+crossSize/2, polygonCenter[1]),
            polygonCenter,
            (polygonCenter[0], polygonCenter[1]-crossSize/2),
            polygonCenter,
            (polygonCenter[0], polygonCenter[1]+crossSize/2),
            polygonCenter
        ]
        graphicalArea.delete_figure(snappedCursor)
        snappedCursor = graphicalArea.draw_polygon(
            crossPoints, line_color='black', line_width=2)
        graphicalArea.delete_figure(tmpCircleAtMouse)
        tmpCircleAtMouse = graphicalArea.draw_circle(
            graphicalArea.snapToGrid(
                graphicalArea.mapPixelToCoords(values['-GRAPH_AREA-'])),
            circleRadius, line_color='black', line_width=1)

    if event == 'Erase':
        graphicalArea.erase()
        graphicalArea.drawGrid()

    if event == 'Save':
        graphicalArea.saveToFile('drawing.png')

    # print(gridResolution)

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()
