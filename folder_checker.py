import os

folders = ['TerminalBasic', 'TerminalBasic/tables', 'TerminalBasic/system', 'TerminalBasic/scripts']
system_folders = ['logs']
logs_files = ['']
system_files = ['module_state']
feedback = ''

def checkfolders():

    feedback = ''

    for i in folders:
        if os.path.exists(f'C:/{i}') == False:
            os.mkdir(f'C:/{i}')
            feedback += f'->Added {i}.\n'

    for i in system_files:
        if os.path.isfile(f'C:/TerminalBasic/system/{i}.txt') == False:
            with open(f'C:/TerminalBasic/system/{i}.txt', 'w') as file:
                if i == 'module_state':
                    file.write('TERMINAL')
            feedback += f'->Added system file {i}.txt.\n'

    # if len(feedback) == 0:
    #     feedback = 'No missing files or directories.'
    #     print('Feedback = 0')
    return feedback


if __name__ == '__main__':
    checkfolders()