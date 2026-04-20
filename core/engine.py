import time, os

from core.loader import load_protocol
from core.parser import normalize
from core.xray_runner import run_xray

from utils.tester import *
from utils.score import score
from utils.table import create_table, color, score_color

from rich.live import Live
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED



def get_name(c):

    if "name" in c and c["name"]:
        return c["name"]

    if "file" in c:
        filename = c["file"].replace("\\", "/").split("/")[-1]

        if "." in filename:
            filename = ".".join(filename.split(".")[:-1])

        return filename

    return "unknown"

def run_engine(link_configs, file_configs, settings, xray):

    all_configs = link_configs + file_configs

    table = create_table()
    results = []

    def worker(original, i):

        name = get_name(original)

        c = normalize(original)

        port = settings["socks_port_start"] + i

        if c["mode"] == "file":

            raw = {
                "file": c["file"],
                "type": c.get("type", "file")
            }

        else:

            proto = load_protocol(c["type"])

            if not proto:
                return None

            try:
                raw = proto.build(c, port)
            except:
                return None

        proc = run_xray(xray, raw)

        start = time.time()
        ok = False

        while True:

            if socks_test(port):
                ok = True
                break

            if time.time() - start > settings["timeout"]:
                break

        try:
            proc.kill()
        except:
            pass

        r = {
            "name": name,
            "type": c.get("type", "file"),
            "socks": ok,
            "dns": dns_test(port),
            "tcp": tcp_test(port),
            "http": http_test(settings["test_url"], port) if ok else False,
            "latency": latency(settings["test_url"], port) if ok else -1
        }

        r["score"] = score(r)

        return r

    def add_row(r):

        table.add_row(
            r["name"],
            r["type"],
            color(r["socks"]),
            color(r["dns"]),
            color(r["tcp"]),
            color(r["http"]),
            str(r["latency"]),
            score_color(r["score"])
        )

    MAX = settings["workers"]

    with Live(table, refresh_per_second=40):

        with ThreadPoolExecutor(max_workers=MAX) as executor:

            pending = []
            i = 0

            while i < len(all_configs) or pending:

                while i < len(all_configs) and len(pending) < MAX:
                    pending.append(executor.submit(worker, all_configs[i], i))
                    i += 1

                done, pending = wait(pending, return_when=FIRST_COMPLETED)
                pending = list(pending)

                for f in done:
                    r = f.result()
                    if r:
                        results.append(r)
                        add_row(r)

    return results