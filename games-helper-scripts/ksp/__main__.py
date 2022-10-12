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
from utils import thousandSeparated

formatter = consolemenu.MenuFormatBuilder(Dimension(width=70, height=40))

formatter.set_header_bottom_padding(0)

formatter.set_items_bottom_padding(0)

formatter.set_footer_bottom_padding(0)

formatter.set_bottom_margin(0)


# Create the menu
menu = ConsoleMenu("KSP, Rockets engineering computation", formatter=formatter)
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
bodiesSelectionMenu = SelectionMenu(bodiesList, "stationary altitute")
SubmenuItem_stationaryAltitude = SubmenuItem(
    "stationary altitute", bodiesSelectionMenu, menu, True)

# Once we're done creating them, we just add the items to the menu
# menu.append_item(menu_item)
# menu.append_item(function_item)
# menu.append_item(command_item)
# menu.append_item(submenu_item)
menu.append_item(SubmenuItem_stationaryAltitude)


restartMenu = True
while restartMenu:

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()
    menu.join()

    mainMenuSelection = menu.selected_option

    if menu.selected_item == menu.exit_item:
        restartMenu = False

    if mainMenuSelection == 0:
        if bodiesSelectionMenu.selected_item != bodiesSelectionMenu.exit_item:
            selectedBody = bodiesList[bodiesSelectionMenu.selected_option]
            print('## Stationary altitude around '+selectedBody+' : ',
                  thousandSeparated(round(stationaryAltitude(KspBody.bodies[selectedBody]))),'meters')
            restartMenu = False


# print(mainMenuSelection)
# print(selectedBody)
