import colorama
from colorama import Fore, Back, Style
import os

colorama.init()

def err(module, type, text):
    print('\n' + Fore.RED + f'{module}_ERROR[{type}]: ' + text + Fore.WHITE + '\n')

def msg(module, type, text):
    if type == 'success':
        print('\n' + Fore.GREEN + f'{module}_MSG: ' + Fore.BLUE + text + Fore.WHITE + '\n')
    elif type == 'warning':
        print('\n' + Fore.YELLOW + f'{module}_WARNING: ' + Fore.BLUE + text + Fore.WHITE + '\n')
    elif type == 'message':
        print('\n' + Fore.MAGENTA + f'{module}_MSG: ' + Fore.BLUE + text + Fore.WHITE + '\n')
    elif type != 'success' and type != 'warning' and type != 'message':
        return 'Unknown type message.'
    
def systemoutput(text):
    print('\n' + Fore.GREEN + "=" * 20 + "COMMAND_OUTPUT" + "=" * 20 + Fore.WHITE + '\n')
    print(text)
    print('\n' + Fore.GREEN + "=" * 53 + Fore.WHITE + '\n')

def sysoutb():
    print('\n' + Fore.GREEN + "=" * 20 + "COMMAND_OUTPUT" + "=" * 20 + Fore.WHITE + '\n')

def sysoute():
    print('\n' + Fore.GREEN + "=" * 53 + Fore.WHITE + '\n')

def terminalcommandlist():

    comm_list = [
        ['status', 'Checks the programs state and system files. ', 'status'],
        ['autofix', 'Restores all the corrupted or missing Terminal Basic system files. ', 'autofix'],
        ['writein','Creates a new file with entered content. ','writein file content > filename'],
        ['chdir', 'Changes current directory. ','chdir folder1/folder2'],
        ['lsdir', 'Shows all directories in the current directory. ','lsdir'],
        ['rmdir', 'Removes directory with entered path. ', 'rmdir folder1/folder2'],
        ['readfile', 'Prints entered file content. ', 'readfile filename'],
        ['clear', 'Clears terminal output. ', 'clear'],
        ['scriptlist', 'Shows all scripts avaible for execution, editing or removing. ','scriptlist'],
        ['scriptexecute', 'Executes a script with entered name. ', 'scriptexecute script_name'],
        ['chmod', 'Brings up a menu with all avaible modules. ', 'chmod'],
        ['moduleinfo', "A quick description to the current module functions and it's purpose. ", 'moduleinfo']
        ]
    
    max_comm = ''

    for i in comm_list:
        if len(i[0]) > len(max_comm):
            max_comm = i[0]

    print()
    for i in range(len(comm_list)):
        print(Fore.CYAN + comm_list[i][0] + Fore.LIGHTWHITE_EX + '-' * (len(max_comm) - len(comm_list[i][0]) + 8) + comm_list[i][1] + Fore.BLUE + 'SYNTAX: ' + Fore.WHITE + comm_list[i][2])
        print()

def csecommandlist():

    comm_list = [
        ['newscript','Creates a new empty script file. ','newscript script_name'],
        ['scriptlist', 'Shows all scripts avaible for execution, editing or removing. ','scriptlist'],
        ['clear', 'Clears terminal output. ', 'clear'],
        ['chmod', 'Brings up a menu with all avaible modules. ', 'chmod'],
        ['moduleinfo', "A quick description to the current module functions and it's purpose. ", 'moduleinfo']
        ]
    
    max_comm = ''

    for i in comm_list:
        if len(i[0]) > len(max_comm):
            max_comm = i[0]

    print()
    for i in range(len(comm_list)):
        print(Fore.CYAN + comm_list[i][0] + Fore.LIGHTWHITE_EX + '-' * (len(max_comm) - len(comm_list[i][0]) + 8) + comm_list[i][1] + Fore.BLUE + 'SYNTAX: ' + Fore.WHITE + comm_list[i][2])
        print()

def stomcommandlist():

    comm_list = [
        ['clear', 'Clears terminal output. ', 'clear'],
        ['chmod', 'Brings up a menu with all avaible modules. ', 'chmod'],
        ['moduleinfo', "A quick description to the current module functions and it's purpose. ", 'moduleinfo']
        ]
    
    max_comm = ''

    for i in comm_list:
        if len(i[0]) > len(max_comm):
            max_comm = i[0]

    print()
    for i in range(len(comm_list)):
        print(Fore.CYAN + comm_list[i][0] + Fore.LIGHTWHITE_EX + '-' * (len(max_comm) - len(comm_list[i][0]) + 8) + comm_list[i][1] + Fore.BLUE + 'SYNTAX: ' + Fore.WHITE + comm_list[i][2])
        print()

def moduleinfo(module):
    if module == 'CSE':
        print('\n'+Fore.BLUE + 'CSE', Fore.GREEN + '(Command Script Editor)' + Fore.WHITE + ':\n')
        print('An editor module which allows the user to write different sets of commands (scripts/instructions) than can be executed through the main module.\n')
    elif module == 'TERMINAL':
        print('\n'+Fore.BLUE + 'Terminal' + Fore.WHITE + ':\n')
        print('Main Terminal Basic module, operates with files and directories inside the machine, executes scripts written in CSE (chmod->CSE->moduleinfo).\n')
    if module == 'STOM':
        print('\n'+Fore.BLUE + 'STOM', Fore.GREEN + '(Simple Tables Operating Module)' + Fore.WHITE + ':\n')
        print('2 deminsional tables editor that is able to create, edit and render tables inside the module.\n(Rendering is done in terminal with basic text deviders (-, +, |))\n')
