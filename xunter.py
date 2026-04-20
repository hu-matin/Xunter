import json
import os

from core.engine import run_engine
from core.xray_path import get_xray_path
from utils.banner import banner
from utils.final_report import generate_report


def main():

    banner()

    settings = json.load(open("settings.json", encoding="utf-8"))

    link_configs = json.load(open("configs.json", encoding="utf-8"))["configs"]

    file_configs = []

    for f in os.listdir("configs"):
        ext = f.split(".")[-1]

        file_configs.append({
            "name": f,
            "file": os.path.join("configs", f),
            "type": ext
        })

    xray = get_xray_path()

    results = run_engine(link_configs, file_configs, settings, xray)

    generate_report(results)


if __name__ == "__main__":
    main()