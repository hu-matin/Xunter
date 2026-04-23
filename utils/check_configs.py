import json
import os

ACTIVE_FILE = "actives.json"


def load_active():
    if not os.path.exists(ACTIVE_FILE):
        return []

    try:
        with open(ACTIVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_active(configs):

    old = load_active()

    existing_raw = set([c["raw"] for c in old if "raw" in c])

    new = []

    for c in configs:
        if c.get("raw") and c["raw"] not in existing_raw:
            new.append(c)

    final = old + new

    with open(ACTIVE_FILE, "w", encoding="utf-8") as f:
        json.dump(final, f, indent=4, ensure_ascii=False)