import os
import file_manager as fm
import system_design as sd
from colorama import Fore

def openscript(inp):
    inp = inp.split()
    inp.remove(inp[0])

    if len(inp) == 0 or inp[0] == '':
        sd.err('CSE', 'CommandStructure', 'Requires 1 argument: script name.')
        return
    else:
        try:
            if os.path.exists("C:/TerminalBasic/scripts/{inp[0]}") == True:
                os.system(f"vim C:/TerminalBasic/scripts/{inp[0]}")
            else:
                sd.msg("TERMINAL", "warning", "Script requested for editing does not exist. Create new empty script with entered name? [y/n]")
                usr_inp = input()
                if usr_inp == "y" or usr_inp == "Y":
                    os.system(f"vim C:/TerminalBasic/scripts/{inp[0]}")
                else:
                    return
        except:
            sd.msg("TERMINAL", "warning", f"Could not open Vim for script editing.\nMake sure you have Vim installed and added to PATH if you are on Unix-like OS.\nFor installation visit {Fore.MAGENTA}vim.org.{Fore.WHITE}")

def newscript(inp):

    inp = inp.split()
    inp.remove(inp[0])

    if len(inp) == 0 or inp[0] == '':
        sd.err('CSE', 'CommandStructure', 'Requires 1 argument: script name.')
        return
    else:
        with open(f'C:/TerminalBasic/scripts/{inp[0]}', 'w'):
            pass
        sd.msg('CSE', 'success', f"New script '{inp[0]}' successfuly created.")

def scriptlist(inp):

    inp = inp.split()
    inp.remove(inp[0])

    if len(inp) != 0:
        sd.err('CSE', 'CommandStructure', 'Command requires no arguments.')
    else:
        if len(os.listdir("C:/TerminalBasic/scripts")) == 0:
            sd.err("TERMINAL", "Logic", "No scripts avaible for execution")
            return
        else:
            sd.sysoutb()
            print('Scripts avaible for execution:')
            for i in os.listdir('C:/TerminalBasic/scripts'):
                print(f'\n{i}')
            sd.sysoute()


def cseReadInput(inp):

    command = ''

    for i in range(len(inp)):
        if inp[i] != ' ':
            command += inp[i]
        else:
            break

    if command == 'commandlist':
        sd.csecommandlist()
    elif command == 'newscript':
        newscript(inp)
    elif command == 'scriptlist':
        scriptlist(inp)
    elif command == '':
        return
    elif command == 'moduleinfo':
        sd.moduleinfo('CSE')
    elif command == 'chmod':
        var = fm.wrapper(fm.menu)
        if var == 'Menu abandoned, no dicision made.':
            sd.msg(fm.terminal_state, 'warning', var)
        else:
            fm.terminal_state = var
    elif command == '':
        return
    elif command == 'clear':
        os.system('cls')
        print()
    else:
        sd.err(fm.state,'CommandStructure', f"'{command}' is not recognized as a command.")
