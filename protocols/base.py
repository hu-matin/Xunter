class BaseProtocol:
    def parse(self, raw): raise NotImplementedError
    def build(self, data): raise NotImplementedError