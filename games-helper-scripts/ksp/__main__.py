# Import the necessary packages
import math
import consolemenu
from consolemenu import *
from consolemenu.items import *
from consolemenu.menu_component import Dimension

from scipy.constants import g

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

# Once we're done creating them, we just add the items to the menu
# menu.append_item(menu_item)
# menu.append_item(function_item)
# menu.append_item(command_item)
# menu.append_item(submenu_item)
menu.append_item(SubmenuItem(
    "stationary altitute", bodiesSelectionMenu, menu, True))
menu.append_item(SubmenuItem(
    "inclination change", bodiesSelectionMenu, menu, True))
menu.append_item(SubmenuItem(
    "Orbital transfer", bodiesSelectionMenu, menu, True))

RESULTS_ERROR_MARGIN = 1.1  # 10 %

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

            deltaVToFinalTarget = getDeltavFromInitialOrbitToTarget(
                centralBody, centralBody.atmoHeight, altitude, 0)
            reachingSpaceComputation = centralBody.reachingSpaceCompute()

            print('## delta V from ground to Stationary altitude (+10% margin for error) :', thousandSeparated(round(
                (reachingSpaceComputation['deltaV_from_ground_to_lowestOrbit'] +
                 deltaVToFinalTarget)*RESULTS_ERROR_MARGIN
            )), 'm/s',

                '('+thousandSeparated(round(
                    reachingSpaceComputation['deltaV_from_ground_to_lowestOrbit'] *
                    RESULTS_ERROR_MARGIN
                )), 'to escape atmosphere +', thousandSeparated(round(deltaVToFinalTarget*RESULTS_ERROR_MARGIN)), 'for final orbit transfer )')

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
                centralBody, apoapsisAltitude, periapsisAltitude, angle)), 'm/s')

    if mainMenuSelection == 2:
        if itemSelected(bodiesSelectionMenu):
            centralBody = getSelectedBody()
            print('Orbital transfer around ' + centralBody.name)

            initialAltitude = float(removeThousandSeparator(
                input('Initial Altitude (km) : ')))*1000
            targetAltitude = float(removeThousandSeparator(
                input('Target Altitude (km) : ')))*1000
            inclinationChange = float(input('Inclination Change (degrees) : '))

            # transferDeltaV = getDeltavFromInitialOrbitToTarget(
            #     centralBody, initialAltitude, targetAltitude, inclinationChange)

            targetOrbitalSpeed = orbitalSpeed(
                centralBody, targetAltitude, targetAltitude)

            print('\n## Orbital speed at', thousandSeparated(int(targetAltitude)), 'm :', thousandSeparated(
                round(targetOrbitalSpeed)), 'm/s')

            if initialAltitude == 0:

                print('\natmosphere height :', centralBody.atmoHeight, 'm')
                print('acceleration assuming 2 TWR :',
                      g, 'm/s²')

                reachingSpaceComputation = centralBody.reachingSpaceCompute()
                timeToReachSpace = reachingSpaceComputation['timeToReach']
                deltaVtoReachSpace = reachingSpaceComputation['deltaVToReach']
                speedUponReachingSpace = reachingSpaceComputation['speedUponReachingSpace']
                wasteddeltaV = reachingSpaceComputation['wasteddeltaV']
                print('timeToReachSpace :', round(timeToReachSpace), 's')
                print('speedUponReachingSpace :', round(
                    speedUponReachingSpace), 'm/s')
                print('wasted delta V :', round(wasteddeltaV), 'm/s')

                deltaVToFinalTarget = getDeltavFromInitialOrbitToTarget(
                    centralBody, centralBody.atmoHeight, targetAltitude, inclinationChange)
                print('\ndelta V from space edge to target :',
                      thousandSeparated(round(deltaVToFinalTarget)), 'm/s')
                print('\n## delta V from ground to target altitude :',
                      thousandSeparated(round(reachingSpaceComputation['deltaV_from_ground_to_lowestOrbit'] + deltaVToFinalTarget)), 'm/s')

            else:
                print('\n## delta V :', thousandSeparated(
                    round(getDeltavFromInitialOrbitToTarget(centralBody, initialAltitude, targetAltitude, inclinationChange))), 'm/s')


# print(mainMenuSelection)
# print(selectedBody)
