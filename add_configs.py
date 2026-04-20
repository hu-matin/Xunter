import json
import os
import shutil

from colorama import Fore, Style


CONFIG_FILE = "configs.json"
CONFIG_FOLDER = "configs"


def auto_add_new_link_config():

    name = input(Fore.YELLOW + "Enter your config name: " + Style.RESET_ALL)
    type_ = input(Fore.YELLOW + "Enter the type of your config [e.g: vless]: " + Style.RESET_ALL)
    raw = input(Fore.YELLOW + "Enter the config link[e.g: vless://...]: " + Style.RESET_ALL)

    if not os.path.exists(CONFIG_FILE):
        data = {"configs": []}
    else:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    data["configs"].append({
        "name": name,
        "type": type_,
        "raw": raw
    })

    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(Fore.GREEN + "Config added to configs.json sccessfully!" + Style.RESET_ALL)


def add_file_config():

    path = input(Fore.YELLOW + "Enter the file path[e.g: path/to/...]: " + Style.RESET_ALL)

    if not os.path.exists(path):
        print(Fore.RED + "File not found!" + Style.RESET_ALL)
        return

    if not os.path.exists(CONFIG_FOLDER):
        os.makedirs(CONFIG_FOLDER)

    filename = os.path.basename(path)
    dest = os.path.join(CONFIG_FOLDER, filename)

    shutil.copy(path, dest)

    print(Fore.GREEN + f"File copied to {dest} sccessfully!" + Style.RESET_ALL)


def main():

    while True:
        
        print(Fore.CYAN + "\n1) Add new link config to (JSON)" + Style.RESET_ALL)
        print(Fore.CYAN + "2) Add new file config to (configs/) folder" + Style.RESET_ALL)

        choice = input(Fore.YELLOW + "Select [1/2] or type [e] to exit the code: " + Style.RESET_ALL)

        if choice == "1":
            auto_add_new_link_config()

        elif choice == "2":
            add_file_config()

        elif choice == "e".lower():
            break

        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()