import file_manager as fm
import cse
import stom
import system_design as sd
import os
import folder_checker
from time import sleep
from ctypes import windll

myappid = "TerminalBasic"
windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
folder_checker.checkfolders()

try:
    with open('C:/TerminalBasic/system/module_state.txt', 'r') as file:
                state = file.readline().upper()
                old_state = state
except:
     state = 'CORRUPTED'
     old_state = 'CORRUPTED'

if __name__ == "__main__":
    os.system('cls')
    state = fm.terminalReadInput('chmod')
    old_state = state

    sd.msg(state, 'success', f"Welcome! Terminal Basic {state} module engaged. Type 'commandlist' inside module for module command list. Current version: 2.2")

    while True:
            
            try:
                with open('C:/TerminalBasic/system/module_state.txt', 'r') as file:
                    state = file.readline().upper()
            except:
                 state = 'CORRUPTED'
                 old_state = 'CORRUPTED'

            if state == 'MENU ABANDONED, NO DECISION MADE.' or state == 'EXIT':
                os.system('cls')
                sd.msg("TERMINAL", 'warning', 'Exiting Terminal Basic. Have a good one!')
                sleep(2)
                break

            if state == 'CORRUPTED':
                inp = input('<damaged-state>')
                fm.terminalReadInput(inp)

            if state != old_state:
                os.system('cls')
                if state == 'CORRUPTED':
                    sd.msg('TERMINAL', 'warning', "System files damaged, only able to use the terminal. Type 'status' for more information.")
                else:
                    sd.msg(state, 'success', f'Terminal Basic {state} module engaged.')
                    old_state = state

            if state == 'TERMINAL':
                try:
                    inp = input(f'<{os.getcwd()}>')
                    fm.terminalReadInput(inp)
                except KeyboardInterrupt:
                    print()
            elif state == 'CSE':
                try:
                    inp = input(f"[{state}]<{os.getcwd()}>")
                    cse.cseReadInput(inp)
                except KeyboardInterrupt:
                    print()
            elif state == 'STOM':
                try:
                    inp = input(f"[{state}]<{os.getcwd()}>")
                    stom.stomReadInput(inp)
                except KeyboardInterrupt:
                    print()
