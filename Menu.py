#!/bin/python3
# -*- coding: utf-8 -*-
import sys, os, time
from colorama import Back, Fore, Style, init
from simple_term_menu import TerminalMenu
import getpass
__author__ = "FDR - Satcom"
__version__ = '0.1.0'
init(autoreset=True)
os.system('clear')

template = """
 ______ _____  _____                               
|  ____|  __ \|  __ \                              
| |__  | |  | | |__) |___  ___  ___ _ ____   _____ 
|  __| | |  | |  _  // _ \/ __|/ _ \ '__\ \ / / _ \\
| |    | |__| | | \ \  __/\__ \  __/ |   \ V /  __/
|_|    |_____/|_|  \_\___||___/\___|_|    \_/ \___|\n"""

def main():
    main_menu_title = template+" \n FDR - Main Menu\n"
    main_menu_items = ["Wallet Update", "Snapshot Update", "Wallet config preview", "Quit"]
    main_menu_cursor = "FDR > "
    main_menu_cursor_style = ("fg_yellow", "bold")
    main_menu_style = ("standout", "fg_yellow", "bold")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    wallet_menu_title = template+" \n FDR - Wallet Menu\n"
    wallet_menu_items = ["Update Wallet", "Back"]
    wallet_menu_back = False
    wallet_menu = TerminalMenu(
        wallet_menu_items,
        title=wallet_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    update_menu_title = template+" \n FDR - Wallet Menu >> Update Menu\n \n Remember to save your wallet.dat ! we don't know what could happen... \n Are you sure ?"
    update_menu_items = ["Yes", "No"]
    update_menu_back = False
    
    update_menu = TerminalMenu(
        update_menu_items,
        title=update_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    fdrmenu_update_menu_title = template+" \n FDR - FDR Menu >> Update Menu\n Remember to save your wallet.dat ! we don't know what could happen... \n Are you sure ?"
    fdrmenu_update_menu_items = ["Yes", "No"]
    fdrmenu_update_menu_back = False
    
    fdrmenu_update_menu = TerminalMenu(
        fdrmenu_update_menu_items,
        title=fdrmenu_update_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    snap_menu_title = template+" \n FDR - Snapshot Update Menu\n Blockchain Snapshot Update \n Remember to save your wallet.dat ! we don't know what could happen... \n DOWNLOAD CAN'T BE STOPPED AFTER LAUNCH ! \nAre you sure ?"
    snap_menu_items = ["Yes", "No"]
    snap_menu_back = False
    snap_menu = TerminalMenu(
        snap_menu_items,
        title=snap_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()
        if main_sel == 0:
            while not wallet_menu_back:
                wall_sel = wallet_menu.show()
                if wall_sel == 0:
                    while not update_menu_back:
                        print("Wallet Update \n Remember to save your wallet.dat ! we don't know what could happen... \n Are you sure ?")
                        edit_sel = update_menu.show()
                        if edit_sel == 0:
                            print("Updating Wallet...")
                        elif edit_sel == 1:
                            update_menu_back = True
                    update_menu_back = True
                elif wall_sel == 1:
                    wallet_menu_back = True
            wallet_menu_back = False

        elif main_sel == 1:
            while not snap_menu_back:
                edit_sel = snap_menu.show()

                if edit_sel == 0:
                    print("Updating Blockchain Snapshot...")
                    try :
                        user = str(getpass.getuser())
                        if user != "root":
                            folder = str(f"/home/{user}/.fdreserve/")
                            os.system(f"rm -rf {folder}/.lock & rm -rf {folder}/blocks & rm -rf {folder}/chainstate")
                            os.system(f"rm -rf {folder}/db.log & rm -rf {folder}/debug.log & rm -rf {folder}/fee_estimate.dat")
                            os.system(f"rm -rf {folder}/mncache.dat & rm -rf {folder}/peers.dat")
                            os.system(f"wget https://fdreserve.com/downloads/snapshot.zip -P /home/{user}/.fdreserve & unzip snapshot.zip & unzip /home/{user}/.fdreserve/snapshot.zip & rm -f snapshot.zip")
                        else :
                            print("Could not be run as root !")
                    except:
                        print("ERROR : Check Internet, .fdreserve folder permissions")
                    snap_menu_back = True
                elif edit_sel == 1:
                    snap_menu_back = True
            snap_menu_back = False


        elif main_sel == 2:
            print("Work in progess ...")
            time.sleep(5)
        elif main_sel == 3:
            main_menu_exit = True

if __name__ == "__main__":
    main()
