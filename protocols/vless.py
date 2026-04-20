class Protocol:

    def build(self, c, port):

        return {
            "type": "vless",
            "server": c.get("server"),
            "port": c.get("port"),
            "uuid": c.get("uuid"),
            "security": c.get("security", "none"),
            "local_port": port
        }