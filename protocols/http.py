class Protocol:

    def build(self, c, port):

        return {
            "type": "http",
            "server": c.get("server"),
            "port": c.get("port"),
            "local_port": port
        }