import os

while ...:
    login, password = input("Login: "), input("Password: ")
    if login and password == 'admin':
        print("Access permitted\n")
        break
    else:
        print("Access denied:( Try again...")
        continue

print(f'You are now: {os.getcwd()}\nType "info" for commands list')


while ...:
    inp = input()
    match inp:
        case 'info':
            print('''console_dir 'directory' - shows all the files and folders in directory
getsize 'directory' - shows the size of the file in bytes
console_exit - exits the programm''')
        case 'console_dir':
            print("Type in directory(C:\Folder\Folder2\File):\n")
            direction = str(input())
            print(os.listdir(direction))
        case 'getsize':
            print("\nType in directory(C:\Folder\Folder2\File):\n")
            getsizeinp = str(input())
            print(os.path.getsize(getsizeinp), "bytes")
        case "console_exit":
            break