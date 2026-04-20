import json

def score(r):
    s = 0

    if r["socks"]: s += 20
    if r["dns"]: s += 20
    if r["tcp"]: s += 20
    if r["http"]: s += 20
    if r["latency"] < 300: s += 20

    return s


def color_score(s):
    if s >= 80:
        return "[green]Good[/green]"
    elif s >= 50:
        return "[yellow]Notbad[/yellow]"
    else:
        return "[red]Bad[/red]"


def save_active(active):
    with open("actives.json", "w") as f:
        json.dump({"actives": active}, f, indent=4)