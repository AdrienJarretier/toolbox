# Import the necessary packages
import consolemenu
from consolemenu import *
from consolemenu.items import *
from consolemenu.menu_component import Dimension

# from consolemenu.prompt_utils import PromptUtils

# def print_report():
#   screen = Screen()
#   try:
#     screen.println('text')
#   except Exception as e:
#     screen.println("Error printing report: %s" % e)
#   finally:
#     screen.println()
#     PromptUtils(screen).enter_to_continue()

from KspBody import KspBody
from orbitalPeriod import stationaryAltitude
from orbitalSpeed import orbitalSpeed
from requiredDeltaVForOrbit import getDeltavFromInitialOrbitToTarget, inclinationChangeDeltaV
from utils import removeThousandSeparator, thousandSeparated

formatter = consolemenu.MenuFormatBuilder(Dimension(width=70, height=40))

formatter.set_header_bottom_padding(0)

formatter.set_items_bottom_padding(0)

formatter.set_footer_bottom_padding(0)

formatter.set_bottom_margin(0)


# Create the menu
menu = ConsoleMenu("KSP, Rockets engineering computation",
                   formatter=formatter, clear_screen=False)
# Create some items

# # MenuItem is the base class for all items, it doesn't do anything when selected
# menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
# function_item = FunctionItem(
#     "stationary altitute",
#     stationaryAltitude)

# # A CommandItem runs a console command
# command_item = CommandItem("Run a console command",  "touch hello.txt")

# # A SelectionMenu constructs a menu from a list of strings
# selection_menu = SelectionMenu(["item1", "item2", "item3"])

# # A SubmenuItem lets you add a menu (the selection_menu above, for example)
# # as a submenu of another menu
# submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

bodiesList = KspBody.bodiesList()
bodiesSelectionMenu = SelectionMenu(
    bodiesList, "Select the orbiting body", formatter=formatter, clear_screen=False)
SubmenuItem_stationaryAltitude = SubmenuItem(
    "stationary altitute", bodiesSelectionMenu, menu, True)
SubmenuItem_inclinationChange = SubmenuItem(
    "inclination change", bodiesSelectionMenu, menu, True)

# Once we're done creating them, we just add the items to the menu
# menu.append_item(menu_item)
# menu.append_item(function_item)
# menu.append_item(command_item)
# menu.append_item(submenu_item)
menu.append_item(SubmenuItem_stationaryAltitude)
menu.append_item(SubmenuItem_inclinationChange)


restartMenu = True
while restartMenu:

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()
    menu.join()

    mainMenuSelection = menu.selected_option

    if menu.selected_item == menu.exit_item:
        restartMenu = False

    def getSelectedBody() -> KspBody:
        selectedBody = bodiesList[bodiesSelectionMenu.selected_option]
        return KspBody.bodies[selectedBody]

    def itemSelected(selectionMenu: SelectionMenu) -> bool:
        global restartMenu
        if selectionMenu.selected_item != selectionMenu.exit_item:
            restartMenu = False

        return not restartMenu

    if mainMenuSelection == 0:
        if itemSelected(bodiesSelectionMenu):
            centralBody = getSelectedBody()
            altitude = stationaryAltitude(centralBody)

            print('## Stationary altitude around '+centralBody.name+' : ',
                  thousandSeparated(round(altitude)), 'meters')

            transferDeltaV = getDeltavFromInitialOrbitToTarget(centralBody, 0, altitude, 0)
            surfaceOrbitalSpeed = orbitalSpeed(centralBody, altitude, altitude)
            missingSpeedToOrbit = max(surfaceOrbitalSpeed-centralBody.surfaceLinearSpeed(),0)

            print('## delta V from ground to Stationary altitude :',
            thousandSeparated(round( missingSpeedToOrbit+transferDeltaV )), 'm/s')

    if mainMenuSelection == 1:
        if itemSelected(bodiesSelectionMenu):
            centralBody = getSelectedBody()
            print('Inclination change around ' + centralBody.name)
            angle = float(input('Angle (degrees) : '))
            apoapsisAltitude = float(removeThousandSeparator(
                input('Apoapsis Altitude (meters) : ')))
            periapsisAltitude = float(removeThousandSeparator(
                input('Periapsis Altitude (meters) : ')))
            print('\n## delta V :', round(inclinationChangeDeltaV(
                centralBody, apoapsisAltitude, periapsisAltitude, angle), 'm/s'))


# print(mainMenuSelection)
# print(selectedBody)
