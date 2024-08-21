# TerminalBasic.py
# Input and module changing handler.


# Import libraries and TB modules

import file_manager as fm
import cse
import stom
import system_design as sd
import os
import folder_checker
from time import sleep
from ctypes import windll

# 

myappid = "TerminalBasic"
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
folder_checker.checkfolders()

def checkstatechange(state, old_state):
    if state != old_state: # Clear the screen if the state has changed

        os.system("cls")

        if state == 'CORRUPTED':
            sd.msg('TERMINAL', 'warning', "System files damaged, only able to use the terminal. Type 'status' for more information.")

        else:
            sd.msg(state, 'success', f"Terminal Basic {state} module engaged.\nType 'commandlist' inside module for module command list.")
            old_state = state


# Attempting to open module state file in TB root directory, if unable to - corrupted phase

try:

    with open('C:/TerminalBasic/system/module_state.txt', 'r') as file:
        state = file.readline().upper()
        old_state = state
except:
     
     state = 'CORRUPTED'
     old_state = 'CORRUPTED'

# Main section

if __name__ == "__main__":

    os.system('cls')

    state = fm.terminalReadInput('chmod', False) # Bring up the module menu on launch
    old_state = state

    sd.msg(state, 'success', f"Welcome! Terminal Basic {state} module engaged.\nType 'commandlist' inside module for module command list.\nCurrent version: 2.2")

    while True:

        try:
            with open('C:/TerminalBasic/system/module_state.txt', 'r') as file:
                state = file.readline().upper()
                # old_state = state
        except:
            state = 'CORRUPTED'
            old_state = 'CORRUPTED'

        if state == 'MENU ABANDONED, NO DECISION MADE.' or state == 'EXIT': # Exits the program if the "Exit" option is chosen in the module menu

            fm.terminalReadInput("clear", False)

            sd.msg("TERMINAL", 'warning', 'Exiting Terminal Basic. Have a good one!')

            sleep(2)
            break

        if state == 'CORRUPTED': # Doesn't let the user change the module and changes the input hint when the state is corrupted

            inp = input('<damaged-state>')
            fm.terminalReadInput(inp, True)

        if state == 'TERMINAL': # Handle the input with the terminal module command list if the state = TERMINAL
            
            checkstatechange(state, old_state)

            try:
                inp = input(f'<{os.getcwd()}>')
                fm.terminalReadInput(inp, False)

            except KeyboardInterrupt:
                print()

        elif state == 'CSE': # Handle the input with the CSE module command list if the state = CSE

            checkstatechange(state, old_state)

            try:
                inp = input(f"[{state}]<{os.getcwd()}>")
                cse.cseReadInput(inp)

            except KeyboardInterrupt:
                print()

        elif state == 'STOM': # Handle the input with the STOM module command list if the state = STOM

            checkstatechange(state, old_state)

            try:
                inp = input(f"[{state}]<{os.getcwd()}>")
                stom.stomReadInput(inp)
                
            except KeyboardInterrupt:
                print()