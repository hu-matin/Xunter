class Protocol:

    def build(self, c, port):

        return {
            "type": "ss",
            "server": c.get("server"),
            "port": c.get("port"),
            "password": c.get("password"),
            "method": c.get("method", "aes-256-gcm"),
            "local_port": port
        }