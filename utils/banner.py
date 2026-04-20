labels = ["""
██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗
╚██╗██╔╝██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ╚███╔╝ ██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ██╔██╗ ██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██╔╝ ██╗╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """
]


from colorama import Fore, Style
import platform, os, random


OS = platform.uname()[0]

command = "cls" if OS == 'Windows' else "clear"

def banner():
    os.system(command)
    rand = random.randint(0, len(labels) - 1)

    print(Fore.CYAN + labels[rand] + Style.RESET_ALL)
    print(Fore.BLUE + "Telegram: " + Fore.GREEN + "https://t.me/ahunter0" + Style.RESET_ALL)
    print(Fore.BLUE + "Github: " + Fore.GREEN + "https://github.com/hu-matin\n\n" + Style.RESET_ALL)


banner()