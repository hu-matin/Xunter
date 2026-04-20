class Protocol:

    def build(self, c, port):

        return {
            "type": "vmess",
            "server": c.get("server"),
            "port": c.get("port"),
            "uuid": c.get("uuid"),
            "local_port": port
        }