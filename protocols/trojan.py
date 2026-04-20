class Protocol:
    def build(self, c, port):
        return {
            "type": "trojan",
            "port": port,
            "raw": c.get("raw", "")
        }