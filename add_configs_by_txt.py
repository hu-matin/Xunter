import json
import os
import random
import string
from colorama import Fore, Style, init

init()

CONFIG_FILE = "configs.json"


def random_name():
    length = random.randint(6, 8)
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def detect_type(link):
    if "://" in link:
        return link.split("://")[0]
    return "unknown"


def load_json():
    if not os.path.exists(CONFIG_FILE):
        return {"configs": []}

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {"configs": []}


def save_json(data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def extract_configs_from_txt(path):

    if not os.path.exists(path):
        print(Fore.RED + "File not found!" + Style.RESET_ALL)
        return

    data = load_json()

    added = 0

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if "://" not in line:
            continue

        name = random_name()
        type_ = detect_type(line)

        config_obj = {
            "name": name,
            "type": type_,
            "raw": line
        }

        data["configs"].append(config_obj)
        added += 1

    save_json(data)

    print(f"{Fore.GREEN}{added} configs added to configs.json{Style.RESET_ALL}")


def main():

    path = input(Fore.YELLOW + "Enter path to txt file: " + Style.RESET_ALL)

    extract_configs_from_txt(path)


if __name__ == "__main__":
    main()