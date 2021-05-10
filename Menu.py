#!/bin/python3
# -*- coding: utf-8 -*-
#### START ANTI QUIT ####
import signal

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGTSTP, signal.SIG_IGN)
#### END ANTI QUIT ####

import getpass
import json
import os
import sys
import time

from colorclass import Color, Windows
from pycoingecko import CoinGeckoAPI
from simple_term_menu import TerminalMenu
from terminaltables import SingleTable

try:
    cg = CoinGeckoAPI()
except Exception as err:
    print(err)
    exit
import socket

__author__ = "FDR - Satcom"
__version__ = "0.9.0"
os.system("clear")
print(
    """
                                       88880000GGGGGGGG000888                                       
                                 8800GCCLLffffttttttt11111tttfLCG08                                 
                             880GCCLLLLLfffffffftttttt1111111iiii1tfLG88                            
                         880GGCCCCCLLLLLLLLfffffffttttttt1111111iiiiii1tLG8                         
                      880GGCCCCCCCCCCLLLLLLLLfffffffttttttt1111111iiiiiiii1fG8                      
                    80GGGGGGGGCCCCCCCCCLLLLLLLfffffffttttttt1111111iiiiiiiiii1L08                   
                  80GGGGGGGGGG0000000000000000000GGGGGGGGGGGGGGGCCCCCCCCCtiiiiiifG8                 
                8GGCGGGGGGGGGG                                           Liiiiii;itG8               
              8GCCCCCGGGGGGGG0                                           LiiiiiiiiiitG              
            8GCCCCCCCCCGGGGGG0                                           L11iiiiiiiiiif0            
           0CLLCCCCCCCCCCGGGGG                                           C1111iiiiiiiii1G           
         8GLLLLLCCCCCCCCCCCGGG          0000000000000GGGGGGGGGGGGGGCCCCCCf111111iiiiiiiiiL8         
        8CLLLLLLLLLCCCCCCCCCCG          GGGCCCCCCCCCCLLLLLLLffffffftttttttt1111111iiiiiiiif8        
       8CfffLLLLLLLLLCCCCCCCCG          GGGGGGCCCCCCCCCLLLLLLLLfffffffttttttt1111111iiiiiiif8       
      8CffffffLLLLLLLLLCCCCCCG          GGGGGGGGCCCCCCCCCLLLLLLLLfffffffttttttt1111111iiiiiif8      
      CtffffffffLLLLLLCCCCCCCG          GGGGGGGGGGGGCCCCCCCLLLLLLLLfffffffttttttt1111111iiiiiL      
     GttttffffffffLL0888888888          8888888888888888GCCCCLLLLLLLLfffffffttttttt1111111iiiiG     
    8fttttttfffffffL8                                   0CCCCCCLLLLLLLLfffffffttttttt1111111iit8    
    C1ttttttttfffffL8                                   0CCCCCCCCLLLLLLLLfffffffttttttt1111111iL    
   8t111ttttttttffffG000000000          8008888888888888GCCCCCCCCCCLLLLLLLLfffffffttttttt111111t8   
   G111111ttttttttffffffffLLLC         8GCCCCCGGGGGGGGGGGGGGCCCCCCCCCLLLLLLLLfffffffttttttt11111G   
   C11111111ttttttttfffffffffC         8CCCCCCCCGGGGGGGGGGGGGGCCCCCCCCCLLLLLLLLfffffffttttttt111C   
   fii11111111ttttttffffffLLLC         8GCCCCCGGGGGGGGGGGGGGGGGGCCCCCCCCCLLLLLLLLfffffffttttttt1L   
   fiiii11111111tttf0888888888          88888888888888880GGGGGGGGGCCCCCCCCCLLLLLLLLfffffffttttttL   
   fiiiiii11111111tf8                                   0GGGGGGGGGGGCCCCCCCCCLLLLLLLLfffffffttttL   
   fiiiiiiii1111111t8                                   0GGGGGGGGGGGGGCCCCCCCCCLLLLLLLLfffffffttC   
   Liiiiiiiiii11111tCGGGGGGGG0          0000000000000000GCGGGGGGGGGGGGGGCCCCCCCCCLLLLLLLLfffffftG   
   Gi;iiiiiiiiii11111111tttttL         8LLLLLLLLLCCCCCCCCCCCGGGGGGGGGGGGGGCCCCCCCCCLLLLLLLLfffff0   
   81;;iiiiiiiiiii11111111tttL         8LfLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGGGGGCCCCCCCCCLLLLLLLLffL8   
    L;;;;iiiiiiiiiii111111111f8        8LfffLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGGGGGCCCCCCCCCLLLLLLLLG    
    01;;;;;;iiiiiiiiii1111111f8        8LfffffLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGGGGGCCCCCCCCCLLLLLC8    
     C;;;;;;;;iiiiiiiiii11111f8        8LfffffffLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGGGGGCCCCCCCCCLLL0     
      f;;;;;;;;;iiiiiiiiii111f8        8ftffffffffLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGGGGGCCCCCCCCCG      
      8t;;;;;;;;;iiiiiiiiiiiif8        8ftttffffffffLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGGGGGCCCCCCG8      
       8t;;;;;;;;;;;iiiiiiiiit8        8ftttttffffffffLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGGGGGCCCG8       
        8f;;;;;;;;;;;;iiiiiiit8        8ftttttttffffffffLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGGGGG08        
         8L;;;;;;;;;;;;;iiiiit8        8t1ttttttttffffffffLLLLLLLLLCCCCCCCCCCGGGGGGGGGGGG0          
           C1;;;;;;;;;;;;iiiit8        8t111ttttttttffffffffLLLLLLLLLCCCCCCCCCCGGGGGGGGG8           
            0fi;;;;;;;;;;;;;;t8        8t11111ttttttttffffffffLLLLLLLLLCCCCCCCCCCGGGGG08            
              Gt;;;;;;;;;;;;;t8        8t1111111ttttttttffffffffLLLLLLLLLCCCCCCCCCCGG8              
               8Gt;;;;;;;;;;;t         8ti11111111ttttttttffffffffLLLLLLLLLCCCCCCCG8                
                 8Gti;;;;;;;;iLCCCCCCCCL1iii11111111ttttttttffffffffLLLLLLLLLCCCG8                  
                   80L1;;;;;;;;;;;;;;iiiiiiiii11111111ttttttttffffffffLLLLLLLCG8                    
                      8Gf1;;;;;;;;;;;;iiiiiiiiii11111111ttttttttffffffffLLCG08                      
                         8GLti;;;;;;;;;iiiiiiiiiii11111111ttttttttffffLCG08                         
                            80GLt1i;;;;;;;iiiiiiiiii111111111ttttfLCG08                             
                                 80GCftt1iiiiiiiiiiii1111ttffLCG088                                 
                                       88800GGGGCCCGGGG000888                                       
"""
)
time.sleep(2)
global fdr_dict, impulse_dict, template


def coins_values():
    try:
        fdr_data = cg.get_coin_ticker_by_id("french-digital-reserve")
        # fdr_data=json.dumps(fdr_data, indent=4)
        fdr_dict = {
            "coin_id": fdr_data["tickers"][0]["coin_id"],
            "curr": fdr_data["tickers"][0]["base"],
            "usd_price": fdr_data["tickers"][0]["converted_last"]["usd"],
            "btc_price": fdr_data["tickers"][0]["converted_last"]["btc"],
            "fdr_vol": fdr_data["tickers"][0]["volume"],
            "usd_vol": fdr_data["tickers"][0]["converted_volume"]["usd"],
            "btc_vol": fdr_data["tickers"][0]["converted_volume"]["btc"],
        }
        fdr_data = cg.get_coin_ticker_by_id("impulse-by-fdr")
        # fdr_data=json.dumps(fdr_data, indent=4)
        impulse_dict = {
            "coin_id": fdr_data["tickers"][0]["coin_id"],
            "curr": fdr_data["tickers"][0]["base"],
            "usd_price": fdr_data["tickers"][0]["converted_last"]["usd"],
            "btc_price": fdr_data["tickers"][0]["converted_last"]["btc"],
            "impulse_vol": fdr_data["tickers"][0]["volume"],
            "usd_vol": fdr_data["tickers"][0]["converted_volume"]["usd"],
            "btc_vol": fdr_data["tickers"][0]["converted_volume"]["btc"],
        }

        table_data = [
            ["Curreny", "FDR", "IMPULSE"],
            [
                Color("{autoyellow}Price USD{/autoyellow}"),
                f'{fdr_dict["usd_price"]} $',
                f'{impulse_dict["usd_price"]} $',
            ],
            [
                Color("{autored}Price BTC{/autored}"),
                f'{fdr_dict["btc_price"]} BTC',
                f'{impulse_dict["btc_price"]} BTC',
            ],
            [
                Color("{autogreen}Volume 24H{/autogreen}"),
                f'{fdr_dict["fdr_vol"]}',
                f'{impulse_dict["impulse_vol"]}',
            ],
        ]
        table_instance = SingleTable(table_data)
        table_instance.inner_heading_row_border = False
        temp = str(
            """

   _____ _        _            _                     ____   _____ 
  / ____| |      | |          | |                   / __ \ / ____|
 | (___ | |_ __ _| | _____  __| | ___   ___  _ __  | |  | | (___  
  \___ \| __/ _` | |/ / _ \/ _` |/ _ \ / _ \| '__| | |  | |\___ \ 
  ____) | || (_| |   <  __/ (_| | (_) | (_) | |    | |__| |____) |
 |_____/ \__\__,_|_|\_\___|\__,_|\___/ \___/|_|     \____/|_____/ 
                                                                     by FDR -- V0.9.0\n\n"""
            + table_instance.table
        )
        return temp
    except:
        return str(
            """

   _____ _        _            _                     ____   _____ 
  / ____| |      | |          | |                   / __ \ / ____|
 | (___ | |_ __ _| | _____  __| | ___   ___  _ __  | |  | | (___  
  \___ \| __/ _` | |/ / _ \/ _` |/ _ \ / _ \| '__| | |  | |\___ \ 
  ____) | || (_| |   <  __/ (_| | (_) | (_) | |    | |__| |____) |
 |_____/ \__\__,_|_|\_\___|\__,_|\___/ \___/|_|     \____/|_____/ 
                                                                     by FDR -- V0.9.0\n\n
    No Connection !
    """
        )


def main():
    """Main function."""
    # coins_values()
    template = coins_values()
    print(template)
    main_menu_title = " \n FDR - Main Menu\n"
    main_menu_items = [
        "Wallet Update",
        "Snapshot Update",
        "FDRMenu Update",
        "Wallet config preview",
        "Browser",
        "Edit Config",
        "Linux Things",
        "Restart Menu",
    ]
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
    wallet_menu_items = ["Open Wallet", "Update Wallet", "Back"]
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
    linux_menu_items = [
        "Upgrade Packets",
        "Repair Network",
        "Reboot",
        "Change Password",
        "Enable SSH",
        "Disable SSH",
        "Local IP",
        "Filezilla",
        "Back",
    ]
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
    fileedit_menu_items = [
        "Edit masternode.conf",
        "Edit fdreserve.conf",
        "Edit Notepad",
        "Back",
    ]
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
                    print("Starting  wallet ...")
                    user = str(getpass.getuser())
                    os.system(f"startx /home/{user}/FDRWallet/fdreserve-qt")
                if wall_sel == 1:
                    while not update_menu_back:
                        print(
                            "Wallet Update \n Remember to save your wallet.dat ! we don't know what could happen... \n Are you sure ?"
                        )
                        edit_sel = update_menu.show()
                        if edit_sel == 0:
                            print("Updating Wallet...")
                        elif edit_sel == 1:
                            update_menu_back = True
                    update_menu_back = True
                elif wall_sel == 2:
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
                                f"rm -rf {folder}/.lock & rm -rf {folder}/blocks & rm -rf {folder}/chainstate"
                            )
                            os.system(
                                f"rm -rf {folder}/db.log & rm -rf {folder}/debug.log & rm -rf {folder}/fee_estimate.dat"
                            )
                            os.system(
                                f"rm -rf {folder}/mncache.dat & rm -rf {folder}/peers.dat"
                            )
                            os.system(
                                f"wget https://fdreserve.com/downloads/snapshot.zip -P /home/{user}/.fdreserve & unzip snapshot.zip & unzip /home/{user}/.fdreserve/snapshot.zip & rm -f snapshot.zip"
                            )
                        else:
                            print("Could not be run as root !")
                    except:
                        print("ERROR : Check Internet Connexion")
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
                        os.system("git pull")
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
                    # while not editconfig_menu_back:
                    user = str(getpass.getuser())
                    listing = []
                    listing.append(f"/home/{user}/.fdreserve/masternode.conf")
                    listing.append(f"/home/{user}/.fdreserve/fdreserve.conf")
                    terminal_menu_test = TerminalMenu(
                        listing,
                        preview_command="batcat --color=always {}",
                        preview_size=0.75,
                    )
                    menu_entry_index = terminal_menu_test.show()
                    terminal_menu_test_back = True
                    editconfig_menu_back = True
                elif linux_sel == 1:
                    linux_sel = 1
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
                        "sudo apt update && sudo apt upgrade && sudo apt autoclean && sleep 1 && clear"
                    )
                    linux_menu_back = True
                elif linux_sel == 1:
                    os.system("sudo systemctl restart networking ")
                    # sudo dhclient
                    linux_menu_back = True
                elif linux_sel == 2:
                    os.system("sudo reboot")
                    linux_menu_back = True
                elif linux_sel == 3:
                    print("Change fdr user password:")
                    os.system("sudo passwd fdr")
                    linux_menu_back = True
                elif linux_sel == 4:
                    print(
                        "Turn on SSH, remember that using ssh create attacks vectors ! \n SSH ports are 22 on IPV4/IPV6"
                    )
                    time.sleep(2)
                    ans = input("ARE YOU SURE ? (YES/NO)")
                    if ans == "YES":
                        os.system(
                            "sudo ufw allow ssh && sudo ufw enable && sudo ufw reload && sudo systemctl restart ssh"
                        )
                    else:
                        linux_menu_back = True
                    linux_menu_back = True
                elif linux_sel == 5:
                    try:
                        os.system(
                            "sudo systemctl stop ssh && sudo ufw delete allow ssh && sudo ufw reload"
                        )
                        print("SSH disabled and firewall ports closed")
                    except:
                        print("An error occurred")
                    linux_menu_back = True
                elif linux_sel == 6:
                    try:
                        hostname = socket.gethostname()
                        local_ip = socket.gethostbyname(hostname)
                        print(local_ip)
                        time.sleep(5)
                        linux_menu_back = True
                    except:
                        print("An error occurred")
                        linux_menu_back = True
                elif linux_sel == 7:
                    try:
                        print("Starting Filezilla ...")
                        os.system("startx filezilla")
                    except:
                        print("Error")
                    linux_menu_back = True
                elif linux_sel == 8:
                    try:
                        from datetime import datetime

                        now = datetime.now()
                        user = str(getpass.getuser())
                        ts = datetime.datetime.now().timestamp()
                        print(
                            f"Duplicating wallet.dat ... \nWallet will be saved in /home/{user}/Wallet-Saves/wallet-{ts}.dat"
                        )
                        os.system(
                            f"cp -f /home/{user}/.fdreserve/wallet.dat /home/{user}/Wallet-Saves/wallet-{ts}.dat "
                        )
                    except:
                        print("Error")
                    linux_menu_back = True
                elif linux_sel == 9:
                    linux_menu_back = True
            linux_menu_back = False

        elif main_sel == 7:

            exit(0)
            main_menu_exit = True


if __name__ == "__main__":
    # while True:
    #     main()
    main()
