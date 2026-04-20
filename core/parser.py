def normalize(c):

    ctype = c.get("type")

    is_file = "file" in c or ctype in [
        "npvtsub", "hat", "hc", "darktunnel", "slipnet"
    ]

    if is_file:
        return {
            "mode": "file",
            "type": ctype,
            "file": c.get("file")
        }

    return {
        "mode": "link",
        "type": ctype,
        "server": c.get("server"),
        "port": c.get("port"),
        "uuid": c.get("uuid"),
        "password": c.get("password"),
        "method": c.get("method")
    }