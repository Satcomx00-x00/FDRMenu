#!/bin/python3
# -*- coding: utf-8 -*-
#### START ANTI QUIT ####
import signal
# signal.signal(signal.SIGINT, signal.SIG_IGN)
# signal.signal(signal.SIGTSTP, signal.SIG_IGN)
#### END ANTI QUIT ####

import sys
import os
import time
from simple_term_menu import TerminalMenu
import getpass
from pycoingecko import CoinGeckoAPI
import json
from terminaltables import SingleTable
from colorclass import Color, Windows
try:
    cg = CoinGeckoAPI()
except Exception as err:
    print(err)
    exit

__author__ = "FDR - Satcom"
__version__ = '0.1.0'
os.system('clear')


global fdr_dict, impulse_dict, template


def coins_values():
    try:

        fdr_data = cg.get_coin_ticker_by_id('french-digital-reserve')
        # fdr_data=json.dumps(fdr_data, indent=4)
        fdr_dict = {
            "coin_id": fdr_data["tickers"][0]["coin_id"],
            "curr": fdr_data["tickers"][0]["base"],
            "usd_price": fdr_data["tickers"][0]["converted_last"]["usd"],
            "btc_price": fdr_data["tickers"][0]["converted_last"]["btc"],
            "fdr_vol": fdr_data["tickers"][0]["volume"],
            "usd_vol": fdr_data["tickers"][0]["converted_volume"]["usd"],
            "btc_vol": fdr_data["tickers"][0]["converted_volume"]["btc"]

        }
        fdr_data = cg.get_coin_ticker_by_id('impulse-by-fdr')
        # fdr_data=json.dumps(fdr_data, indent=4)
        impulse_dict = {
            "coin_id": fdr_data["tickers"][0]["coin_id"],
            "curr": fdr_data["tickers"][0]["base"],
            "usd_price": fdr_data["tickers"][0]["converted_last"]["usd"],
            "btc_price": fdr_data["tickers"][0]["converted_last"]["btc"],
            "impulse_vol": fdr_data["tickers"][0]["volume"],
            "usd_vol": fdr_data["tickers"][0]["converted_volume"]["usd"],
            "btc_vol": fdr_data["tickers"][0]["converted_volume"]["btc"]
        }

        table_data = [
            ['Curreny', 'FDR', 'IMPULSE'],
            [Color('{autoyellow}Price USD{/autoyellow}'),
             f'{fdr_dict["usd_price"]} $', f'{impulse_dict["usd_price"]} $'],
            [Color('{autored}Price BTC{/autored}'),
             f'{fdr_dict["btc_price"]} BTC', f'{impulse_dict["btc_price"]} BTC'],
            [Color('{autogreen}Volume 24H{/autogreen}'),
             f'{fdr_dict["fdr_vol"]}', f'{impulse_dict["impulse_vol"]}'],
        ]
        table_instance = SingleTable(table_data)
        table_instance.inner_heading_row_border = False
        temp = str("""
                                                     .--------.
                                                    / .------. \\
                                                   / /        \ \\
                                                   | |        | |
                                                  _| |________| |_
                                                .' |_|        |_| '.
 _____ ____  ____   __     __          _ _      '._____ ____ _____.'
|  ___|  _ \|  _ \  \ \   / /_ _ _   _| | |_    |     .'____'.     |
| |_  | | | | |_) |  \ \ / / _` | | | | | __|   '.__.'.'    '.'.__.'
|  _| | |_| |  _ <    \ V / (_| | |_| | | |_    '.__  | VAULT | __.'
|_|   |____/|_| \_\    \_/ \__,_|\__,_|_|\__|   |   '.'.____.'.'   |
                                                '.____'.____.'____.'
                                                '.________________.'  by FDR\n\n""" + table_instance.table)
        return temp
    except:
        return str("""
                                                     .--------.
                                                    / .------. \\
                                                   / /        \ \\
                                                   | |        | |
                                                  _| |________| |_
                                                .' |_|        |_| '.
 _____ ____  ____   __     __          _ _      '._____ ____ _____.'
|  ___|  _ \|  _ \  \ \   / /_ _ _   _| | |_    |     .'____'.     |
| |_  | | | | |_) |  \ \ / / _` | | | | | __|   '.__.'.'    '.'.__.'
|  _| | |_| |  _ <    \ V / (_| | |_| | | |_    '.__  | VAULT | __.'
|_|   |____/|_| \_\    \_/ \__,_|\__,_|_|\__|   |   '.'.____.'.'   |
                                                '.____'.____.'____.'
                                                '.________________.'  by FDR\n\n
    No Connection !
    """)



def main():
    """Main function."""
    # coins_values()
    template = coins_values()
    print(template)
    main_menu_title = " \n FDR - Main Menu\n"
    main_menu_items = ["Wallet Update", "Snapshot Update", "FDRMenu Update",
                       "Wallet config preview", "Browser", "Edit Config", "Linux Things", "Restart Menu"]
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
        clear_screen=False,
    )
    wallet_menu_title = " \n FDR - Wallet Menu\n"
    wallet_menu_items = ["Update Wallet", "Back"]
    wallet_menu_back = False
    wallet_menu = TerminalMenu(
        wallet_menu_items,
        title=wallet_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )

    update_menu_title = " \n FDR - Wallet Menu >> Update Menu\n \n Remember to save your wallet.dat ! we don't know what could happen... \n Are you sure ?"
    update_menu_items = ["Yes", "No"]
    update_menu_back = False

    update_menu = TerminalMenu(
        update_menu_items,
        title=update_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )

    fdrmenu_update_menu_title = " \n FDR - FDR Menu >> Update Menu\n Are you sure ?"
    fdrmenu_update_menu_items = ["Yes", "No"]
    fdrmenu_update_menu_back = False

    fdrmenu_update_menu = TerminalMenu(
        fdrmenu_update_menu_items,
        title=fdrmenu_update_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )

    snap_menu_title = " \n FDR - Snapshot Update Menu\n Blockchain Snapshot Update \n Remember to save your wallet.dat ! we don't know what could happen... \n DOWNLOAD CAN'T BE STOPPED AFTER LAUNCH ! \nAre you sure ?"
    snap_menu_items = ["Yes", "No"]
    snap_menu_back = False
    snap_menu = TerminalMenu(
        snap_menu_items,
        title=snap_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )

    browser_menu_title = " \n FDR - Browser Menu\n"
    browser_menu_items = ["Brave", "TOR", "Back"]
    browser_menu_back = False
    browser_menu = TerminalMenu(
        browser_menu_items,
        title=browser_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )

    editconfig_menu_title = " \n FDR - Linux Command Menu\n"
    editconfig_menu_items = ["Get FDR wallet config file", "Back"]
    editconfig_menu_back = False
    editconfig_menu = TerminalMenu(
        editconfig_menu_items,
        title=editconfig_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )
    

    linux_menu_title = " \n FDR - Linux Command Menu\n"
    linux_menu_items = ["Upgrade Packets",
                        "Repair Network", "Reboot", "Change Password", "Enable SSH", "Disable SSH","Back"]
    linux_menu_back = False
    linux_menu = TerminalMenu(
        linux_menu_items,
        title=linux_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )

    fileedit_menu_title = " \n FDR - File Edit Menu\n"
    fileedit_menu_items = ["Edit masternode.conf", "Edit fdreserve.conf", "Edit  Notepad", "Back"]
    fileedit_menu_back = False
    fileedit_menu = TerminalMenu(
        fileedit_menu_items,
        title=fileedit_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()
        if main_sel == 0:
            while not wallet_menu_back:
                wall_sel = wallet_menu.show()
                if wall_sel == 0:
                    while not update_menu_back:
                        print(
                            "Wallet Update \n Remember to save your wallet.dat ! we don't know what could happen... \n Are you sure ?")
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
                    try:
                        user = str(getpass.getuser())
                        if user != "root":
                            folder = str(f"/home/{user}/.fdreserve/")
                            os.system(
                                f"rm -rf {folder}/.lock & rm -rf {folder}/blocks & rm -rf {folder}/chainstate")
                            os.system(
                                f"rm -rf {folder}/db.log & rm -rf {folder}/debug.log & rm -rf {folder}/fee_estimate.dat")
                            os.system(
                                f"rm -rf {folder}/mncache.dat & rm -rf {folder}/peers.dat")
                            os.system(
                                f"wget https://fdreserve.com/downloads/snapshot.zip -P /home/{user}/.fdreserve & unzip snapshot.zip & unzip /home/{user}/.fdreserve/snapshot.zip & rm -f snapshot.zip")
                        else:
                            print("Could not be run as root !")
                    except:
                        print("ERROR : Check Internet, .fdreserve folder permissions")
                    snap_menu_back = True
                elif edit_sel == 1:
                    snap_menu_back = True
            snap_menu_back = False

        elif main_sel == 2:
            while not fdrmenu_update_menu_back:
                fdrmenu_update_sel = fdrmenu_update_menu.show()
                if fdrmenu_update_sel == 0:
                    print("Updating Menu...")
                    try:
                        os.system("git merge main")
                        time.sleep(2)
                    except:
                        print("Error on update.")
                        time.sleep(5)
                    fdrmenu_update_menu_back = True
                elif fdrmenu_update_sel == 1:
                    fdrmenu_update_menu_back = True
            fdrmenu_update_menu_back = False

        elif main_sel == 3:
            while not editconfig_menu_back:
                linux_sel = editconfig_menu.show()
                if linux_sel == 0:
                    user = str(getpass.getuser())
                    listing=[]
                    listing.append(f"/home/{user}/.fdreserve/masternode.conf")
                    listing.append(f"/home/{user}/.fdreserve/fdreserve.conf")
                    terminal_menu_test = TerminalMenu(listing, preview_command="batcat --color=always {}", preview_size=0.75)
                    menu_entry_index = terminal_menu_test.show()
                elif fdrmenu_update_sel == 1:
                    editconfig_menu_back = True
                editconfig_menu_back = False

        elif main_sel == 4:
            while not browser_menu_back:
                fdrmenu_update_sel = browser_menu.show()
                if fdrmenu_update_sel == 0:
                    try:
                        print("Starting Brave ...")
                        os.system("startx brave-browser")
                    except:
                        print("Error")
                    browser_menu_back = True
                elif fdrmenu_update_sel == 1:
                    try:
                        print("Starting TOR ...")
                        os.system("startx torbrowser-launcher")
                    except:
                        print("Error")
                    browser_menu_back = True
                elif fdrmenu_update_sel == 2:
                    browser_menu_back = True
            browser_menu_back = False

        elif main_sel == 5:
            while not fileedit_menu_back:
                fileedit_sel = fileedit_menu.show()
                if fileedit_sel == 0:
                    user = str(getpass.getuser())
                    os.system(f"nano /home/{user}/.fdreserve/masternode.conf")
                    fileedit_menu_back = False
                elif fileedit_sel == 1:
                    user = str(getpass.getuser())
                    os.system(f"nano /home/{user}/.fdreserve/fdreserve.conf")
                    fileedit_menu_back = False
                elif fileedit_sel == 2:
                    os.system(f"nano /home/{user}/notepad.txt")
                    fileedit_menu_back = True
                elif fileedit_sel == 3:
                    fileedit_menu_back = True
            fileedit_menu_back = False
            

        elif main_sel == 6:
            while not linux_menu_back:
                linux_sel = linux_menu.show()
                if linux_sel == 0:
                    os.system(
                        "sudo apt update && sudo apt upgrade && sudo apt autoclean && sleep 1 && clear")
                    linux_menu_back = True
                elif linux_sel == 1:
                    os.system(
                        "sudo systemctl restart networking && sudo dhclient")
                    linux_menu_back = True
                elif linux_sel == 2:
                    os.system("sudo reboot")
                    linux_menu_back = True
                elif linux_sel == 3:
                    print("Change fdr user password:")
                    os.system("sudo passwd fdr")
                    linux_menu_back = True
                elif linux_sel == 4:
                    print("Turn on SSH, remember that using ssh create attack vectors ! \n SSH ports are 22 on IPV4/IPV6")
                    time.sleep(2)
                    ans = input("ARE YOU SURE ? (YES/NO)")
                    if ans == "YES":
                        os.system("sudo ufw allow ssh && sudo ufw reload && sudo systemctl start ssh")
                    else:
                        linux_menu_back = True
                    linux_menu_back = True
                elif linux_sel == 5:
                    try :
                        os.system("sudo systemctl stop ssh && sudo ufw delete allow ssh && sudo ufw reload")
                        print("SSH disabled and firewall ports closed")
                    except:
                        print("An error occurred")
                    linux_menu_back = True
                elif linux_sel == 6:
                    linux_menu_back = True
            linux_menu_back = False

        elif main_sel == 7:
            exit(0)
            main_menu_exit = True

if __name__ == "__main__":
    # while True:
    #     main()
    main()
