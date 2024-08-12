import os
import file_manager as fm
import system_design as sd

def stomReadInput(inp):

    command = ''

    for i in range(len(inp)):
        if inp[i] != ' ':
            command += inp[i]
        else:
            break
        

    if command == 'commandlist':
        sd.stomcommandlist()
    elif command == 'moduleinfo':
        sd.moduleinfo('STOM')
    elif command == 'chmod':
        var = fm.wrapper(fm.menu)
        if var == 'Menu abandoned, no dicision made.':
            sd.msg(fm.state, 'warning', var)
        else:
            fm.state = var
    elif command == '':
        return
    elif command == 'clear':
        os.system('cls')
        print()
    else:
        sd.err(fm.state,'CommandStructure', f"'{command}' is not recognized as a command.")