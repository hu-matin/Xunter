class Protocol:

    def build(self, c, port):

        return {
            "type": "socks",
            "server": c.get("server"),
            "port": c.get("port"),
            "local_port": port
        }