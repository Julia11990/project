from Model import *
from View import *

def main():
    choice = display_menu()

    if choice == "1":
        levels_list = get_levels()
        show_levels(levels_list)
    elif choice =="2":

