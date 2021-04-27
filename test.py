#!/usr/bin/env python3
import getpass

import os
from simple_term_menu import TerminalMenu
user = str(getpass.getuser())

def list_files(directory="."):
    return (file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)))


def main():
    listing=[]
    listing.append("/home/satcom/Documents/FDR/owasp_rapprot.html")
    terminal_menu_test = TerminalMenu(listing, preview_command="batcat --color=always {}", preview_size=0.75)
    menu_entry_index = terminal_menu_test.show()


if __name__ == "__main__":
    main()
