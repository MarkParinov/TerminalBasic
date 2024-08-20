# File manger (terminal module command library)

# I am NOT commenting all this, mainly here are just functions for terminal module and input handler

import system_design as sd
import os
from colorama import Fore
import curses
import shutil
from pathlib import Path
from curses import wrapper
import folder_checker

def writein(inp):

    command = ''
    value = ''
    subvalue = ''

    try:

        for i in range(len(inp)):
            if inp[i] != ' ':
                command += inp[i]
            else:
                break

        inp = inp.split()
        inp.remove(inp[0])

        new_inp = inp[:]

        for i in range(len(inp)):
            if inp[i] != '>':
                value += inp[i]
                value += ' '
                new_inp.remove(inp[i])
            else:
                value = value[:-1]
                new_inp.remove(inp[i])
                break

        subvalue = new_inp[-1]

    except:
        sd.err('TERMINAL','CommandStructure', 'Invalid number of arguments. Unable to write in')
        return

    try:
        with open(f'./{subvalue}.txt', 'w') as file:
            file.write(value)
            sd.msg('TERMINAL','success', 'File created.')
    except PermissionError as error:
        sd.err('TERMINAL','Permission', 'Permission to write a file denied.')
        
def changedir(inp):

    value = ''

    try:
        inp = inp.split()
        inp.remove(inp[0])
        value = ''
        for i in inp:
            value += i
            value += ' '
        value = value[:-1]
    except:
        sd.err('TERMINAL','CommandStructure', 'Takes 1 argument, wrong number of arguments was given.')
        return
   
    try:
        if value == '':
            return
        if os.path.isdir(value) == True:
            last_dir = os.getcwd()
            os.chdir(value)
            sd.msg('TERMINAL','success', f'Directory changed. {last_dir} --> {os.getcwd()}')
        else:
            sd.err('TERMINAL','Logic', f"Unable to locate '{value}' as a sub-directory or as an individual path.")
    
    except PermissionError:
        sd.err('TERMINAL', 'Permission', f"Cannot access {value}")

def listdir(inp):
    if len(inp.split()) > 1:
        sd.err('TERMINAL','CommandStructure', 'Command takes no arguments, but some were given.')
    else:
        try:
            dir_table(os.listdir(), os.getcwd())
        except PermissionError as error:
            sd.err('TERMINAL', 'Permission', f'Cannot access {os.getcwd()}')

def totalmemoryindir(memory):

    memory_b = memory

    memory_type = 'bytes'
    if memory > 1024:
        memory //= 1024
        memory_type = 'kilobytes'
        if memory > 1024:
            memory //= 1024
            memory_type = 'megabytes'
            if memory > 1024:
                memory //= 1024
                memory_type = 'gigabytes'
    
    if memory_type == 'bytes':
        print(Fore.WHITE + 'Total of' + Fore.MAGENTA, memory, Fore.WHITE + f'{memory_type} worth of files in {os.getcwd()}')
    else:
        print(Fore.WHITE + 'Total of' + Fore.MAGENTA, memory, Fore.WHITE + f'{memory_type} ({Fore.MAGENTA}{memory_b}{Fore.WHITE} bytes) worth of files in {os.getcwd()}')

def dir_table(dirs, path):

    files_count = 0
    dirs_count = 0
    dirs_max = ''
    col_max = 'directory'
    total_bytes = 0

    for i in dirs:
        if len(i) > len(dirs_max):
            dirs_max = i

    for i in dirs:
        if os.path.isfile(i) == True:
            try:
                if len(Path(i).suffixes[-1]) > len(col_max):
                    col_max = Path(i).suffixes[-1]
            except:
                if len('unknown type') > len(col_max):
                    col_max = 'unknown type'

    print()
    max_ext = len('directory')
    for i in dirs:
        if os.path.isfile(i) == True:
            file = i.split('.')
            file.remove(file[0])
            try:
                if len(file[0]) > max_ext:
                        max_ext = len(file[0])
            except:
                if len('unknown type') > max_ext:
                        max_ext = len('unknown type')
    for i in dirs:
        try:
            if os.path.isdir(i) == True:
                dirs_count += 1
                sub_dirs = os.listdir(f'./{i}')
                print(Fore.BLUE + i + ' ' * (len(dirs_max) - len(i) + 5), end='')
                print(Fore.MAGENTA + 'directory' + (' ' * (len(col_max) - 4)) + Fore.MAGENTA, len(sub_dirs), Fore.WHITE + 'sub-directories and files')
                
            else:
                
                suffs = Path(i).suffixes
                if suffs == []:
                    suffs = ['unknown type']
                files_count += 1
                file = i.split('.')
                file.remove(file[0])
                print(Fore.BLUE + i + ' ' * (len(dirs_max) - len(i) + 5), end='')
                print(Fore.GREEN + f'{suffs[-1]} file{Fore.WHITE}' + (' ' * (len(col_max) - len(suffs[-1]))) + Fore.MAGENTA, os.path.getsize(f'{i}'), Fore.WHITE + 'bytes')
                total_bytes += os.path.getsize(f'./{i}')
        except:
            print(f'{Fore.RED}Cannot access {i} in {path}.{Fore.WHITE}')
        
    print()
    totalmemoryindir(total_bytes)
    print()
    print(f'{Fore.MAGENTA}{files_count}{Fore.WHITE} files, {Fore.MAGENTA}{dirs_count}{Fore.WHITE} directories.')
    print()

def readfile(inp):

    try:
        inp = inp.split()
        inp.remove(inp[0])
    except:
        sd.err('TERMINAL','CommandStructure', 'Command takes 1 argument.')
        return
    
    if len(inp) == 0:
        sd.err('TERMINAL','CommandStructure', 'Command takes 1 argument.')
        return

    
    if os.path.isfile(f"./{inp[0]}") == True:
        try:
            with open(f'./{inp[0]}', 'r') as file:
                sd.systemoutput(file.read())
        except:
            sd.err('TERMINAL','Unknown', f"'{inp[0]}': An unknown error has occured while reading the file. Check the file's content and try again.")
    elif os.path.isdir(f"./{inp[0]}") == True:
        sd.err('TERMINAL', 'Logic', f"'{inp[0]}': unable to read a directory.")

    else:
        sd.err('TERMINAL', 'Logic', f"'{inp[0]}': file is unreadable or doesn't exist. Check the spelling and the extension of the file.")


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


def scriptexecute(inp):

    inp = inp.split()
    inp.remove(inp[0])

    if len(inp) == 0 or inp[0] == '':
        sd.err('CSE', 'CommandStructure', 'Requires 1 argument: script name.')
        return
    if os.path.exists(f'C:/TerminalBasic/scripts/{inp[0]}') == False:
        sd.err('CSE', 'Logic', f"'{inp[0]}': script does not exist.")
        return
    with open(f'C:/TerminalBasic/scripts/{inp[0]}', 'r+') as script:
        feedback = []
        for i in script.readlines():
            line = i.rstrip()
            try:
                terminalReadInput(line)
                feedback += [line]
            except:
                sd.err('CSE', 'CommandStructure', f"'{line}': invalid command structure.")
                return
    os.system('cls')
    sd.msg('CSE', 'success', 'Script executed successfuly. Show executing history? Y/N')
    inp = input()
    if inp == 'Y' or inp == 'y':
        sd.sysoutb()
        for i in feedback:
            print(f'>{i}')
        sd.sysoute()
        return
    else:
        return
    
def rmdir(inp):

    value = ''

    try:
        inp = inp.split()
        inp.remove(inp[0])
        value = ''
        for i in inp:
            value += i
            value += ' '
        value = value[:-1]
    except:
        sd.err('TERMINAL','CommandStructure', 'Takes 1 argument, wrong number of arguments was given.')
        return
    
    try:

        try:
    
            if os.path.isdir(value) == True:
                size = len(os.listdir(value))

                if size > 0:
                    sd.msg('TERMINAL', 'warning', 'Directory requested for removing is not empty!\nAre you sure you want to remove it with all the directories and files in it?\nThis operation is not recallable, the directory will be gone completely.\n[Y/N]')
                    inp = input()
                    if inp == 'Y' or inp == 'y':
                        removed_files = os.listdir(value)
                        shutil.rmtree(value)
                        sd.msg('TERMINAL', 'success', f"'{value}': directory removed succesfuly. Removed objects:")
                        for i in removed_files:
                            print(f'>{i}')
                            if os.path.isdir(i):
                                for n in os.lsdir(i):
                                    print(f'>>{n}')
                        return
                    else:
                        return
                else:
                    os.rmdir(value)
                    sd.msg('TERMINAL', 'success', f"'{value}': empty directory removed succesfuly.")
                    return
            else:
                sd.err('TERMINAL','Logic', f"'{os.getcwd()}\{value}': directory does not exist.")
                return
            
        except PermissionError:

            sd.err("TERMINAL", 'Permission', f"Unable to remove {value}.")
    except:
        sd.err('TERMINAL', 'SystemPerfomance', 'Cannot remove opened directory.')
        return

system_overall_status = 100

def checfunc(text, status):
    max_len = len('Terminal Basic root directory')
    global system_overall_status
    print(f'{Fore.WHITE}{text}:', end='')
    if status == True:
        print(f'{' ' * (max_len - len(text) + 3)}[{Fore.GREEN}OPERATIONAL{Fore.WHITE}]\n')
        return 'operational'
    else:
        print(f'{' ' * (max_len - len(text) + 3)}[{Fore.RED}MISSING{Fore.WHITE}]\n')
        system_overall_status = system_overall_status - (system_overall_status / 5)
        return 'missing'

def status(inp):

    tb_exists = False
    script_folder_exists = False
    system_folder_exists = False
    tables_folder_exists = False
    module_state_exists = False

    system_check = [tb_exists, script_folder_exists, system_folder_exists, tables_folder_exists, module_state_exists]

    if len(inp.split()) > 1:
        sd.err('TERMINAL','CommandStructure', 'Command takes no arguments, but some were given.')
    else:

        if os.path.exists('C:/TerminalBasic') == True:
            tb_exists = True
        if os.path.exists('C:/TerminalBasic/scripts') == True:
            script_folder_exists = True
        if os.path.exists('C:/TerminalBasic/system') == True:
            system_folder_exists = True
        if os.path.exists('C:/TerminalBasic/tables') == True:
            tables_folder_exists = True
        if os.path.exists('C:/TerminalBasic/system/module_state.txt') == True:
            module_state_exists = True
        
        print(f'\n{Fore.MAGENTA}System status:\n')

        stats = []

        stats += [checfunc('Terminal Basic root directory', tb_exists)]
        stats += [checfunc('System directory', system_folder_exists)]
        stats += [checfunc('Scripts directory', script_folder_exists)]
        stats += [checfunc('Tables data directory', tables_folder_exists)]
        stats += [checfunc('Module state file', module_state_exists)]
        if 'missing' in stats:
            sd.msg('TERMINAL', 'warning', "Some system files or directories are corrupted or missing. Autofix advised.\nType 'autofix' for the software to try and fix itself.")
        


#---------------------MENU----------------------#

items = {
    'TERMINAL':'Terminal Basic (main module)',
    'STOM':'Simple Tables Operating Module (STOM)',
    'CSE':'Command Script Editor (CSE)',
    'Exit':'Exit'
    }

keys = list(items.keys())
values = list(items.values())

global greeted_modules
greeted_modules = False

def menu(out):

    # if greeted_modules == False:
    #     title = out.addstr(0, 0, 'Welcome to Terminal Basic! Please, choose a module to begin.', curses.A_BOLD)
    # else:
    #     title = out.addstr(0, 0, 'Choose a module to run.', curses.A_BOLD)

    # title

    x = 0
    item_id = 0

    # for i in range(len(items)):
    #     x += 1
    #     if item_id == i:
    #         out.addstr(x, 0, '>' + items.get(keys[i]), curses.A_REVERSE)
    #     else:
    #         out.addstr(x, 0, items.get(keys[i]))

    # out.refresh()

    key = 1

    while True:

        out.clear()

        global greeted_modules

        if greeted_modules == False:
            title = out.addstr(0, 0, 'Welcome to Terminal Basic! Please, choose a module to begin.', curses.A_BOLD)
        else:
            title = out.addstr(0, 0, 'Choose a module to run.', curses.A_BOLD)

        title

        for i in range(len(items)):
            x += 1
            if item_id == i:
                out.addstr(x, 0, '>' + items.get(keys[i]), curses.A_REVERSE)
            else:
                out.addstr(x, 0, ' ' + items.get(keys[i]))
        out.addstr(x+1, 0, '')

        key = out.getch()
        # out.addstr(5, 5, f'Key: {key}')
        # out.refresh()
        # out.getch()

        if (key == 456 and item_id + 1 <= len(items) - 1) or (key == 258 and item_id + 1 <= len(items) - 1):
            item_id += 1

        if (key == 450 and item_id - 1 >= 0) or (key == 259 and item_id - 1 >= 0):
            item_id -= 1

        if key == 27:
            greeted_modules = True
            out.clear()
            exit()
        
        if key == 10:
            global state
            greeted_modules = True
            state = keys[item_id]
            with open ('C:/TerminalBasic/system/module_state.txt', 'w') as f:
                f.writelines(state)

            return keys[item_id]
        
        x = 0

        out.refresh()

# if __name__ == '__main__':
#     wrapper(menu)

#----------Input readers for modules---------#

def terminalReadInput(inp, damaged):         #Terminal (main)

    command = ''

    for i in range(len(inp)):
        if inp[i] != ' ':
            command += inp[i]
        else:
            break

    if command == 'writein':
        writein(inp)
    elif command == 'chdir':
        changedir(inp)
    elif command == 'lsdir':
        listdir(inp)
    elif command == 'commandlist':
        sd.terminalcommandlist()
    elif command == 'readfile':
        readfile(inp)
    elif command == 'scriptlist':
        scriptlist(inp)
    elif command == 'scriptexecute':
        scriptexecute(inp)
    elif command == 'clear':
        os.system('cls')
        print()
    elif command == 'status':
        status(inp)
    elif command == 'autofix':
        feedback = folder_checker.checkfolders()
        if feedback == '':
            sd.msg('TERMINAL', 'success', 'No missing or corrupted files found.')
        else:
            print(f"\n{Fore.BLUE}Autofix in progress...\n")
            print(f'{Fore.MAGENTA}=====COMMAND FEEDBACK====={Fore.WHITE}\n')
            print(feedback)
            print(f'{Fore.MAGENTA}=========================={Fore.WHITE}\n')
    elif command == 'rmdir':
        rmdir(inp)
    elif command == 'moduleinfo':
        sd.moduleinfo('TERMINAL')
    elif command == 'chmod':
        if damaged == True:
            sd.err("TERMINAL", "System", "Unable to change module while in damaged state.")
            return
        else:
            var = wrapper(menu)
            return var
    elif command == '':
        return
    else:
        sd.err("TERMINAL",'CommandStructure', f"'{command}' is not recognized as a command.")
