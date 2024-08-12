from colorama import Fore

def encodelog(type, usr_side_err, add_soft_req, comm_exec_properly):
    log = ""
    match type:
        case "message":
            log += "0"
        case "warning":
            log += "1"
        case "error":
            log += "2"
        case _:
            log += "%"

    match usr_side_err:
        case True:
            log += "1"
        case False:
            log += "x"
        case _:
            log += "%"

    match add_soft_req:
        case True:
            log += "1"
        case False:
            log += "x"
        case _:
            log += "%"

    match comm_exec_properly:
        case True:
            log += "1"
        case False:
            log += "x"
        case _:
            log += "%"

    

def decodelog(log):
    type = ""
    usr_side_err = False
    add_soft_req = False
    comm_exec_properly = True

    log = log
    match log[0]:   #Get message type
        case "0":
            type = "message"
        case "1":
            type = "warning"
        case "2":
            type = "error"
        case _:
            type = "unknown"

    match log[1]:
        case "x":
            usr_side_err = False
        case "1":
            usr_side_err = True
        case _:
            usr_side_err = "unknown"

    match log[2]:
        case "x":
            add_soft_req = False
        case "1":
            add_soft_req = True
        case _:
            add_soft_req = "unknown"

    match log[3]:
        case "x":
            comm_exec_properly = False
        case "1":
            comm_exec_properly = True
        case _:
            comm_exec_properly = "unknown"

    return [type, usr_side_err, add_soft_req, comm_exec_properly]

def logstatement(log):
    stats = decodelog(log)
    out = ""
    out += f"=={Fore.CYAN}Message Info{Fore.WHITE} (log: {Fore.LIGHTBLUE_EX}{log})==\n\n"
    out += f"Message type: {stats[0]}\n"
    
    if stats[1] == True:
        out += f"{Fore.MAGENTA}>>{Fore.LIGHTRED_EX}User-sided error.\n"
    if stats[2] == True:
        out += f"{Fore.MAGENTA}>>{Fore.LIGHTRED_EX}Additional software has to be installed.\n"
    if stats[3] == False:
        out += f"{Fore.MAGENTA}>>{Fore.LIGHTRED_EX}Command was exectuted improperly."
    
    out += f"{Fore.WHITE}"
    return out