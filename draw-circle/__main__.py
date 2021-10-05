import PySimpleGUI as sg
from GrisBasedGraph import GrisBasedGraph

graphicalArea = GrisBasedGraph((3, 3), (40, 40))

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

graphicalArea.drawGrid()

# circleId = graphicalArea.draw_circle(
#     (0, 0), 50, line_color='black', line_width=4)

# print('circle id :', circleId)

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
