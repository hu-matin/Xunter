import importlib
from core.registry import PROTOCOLS


def load_protocol(name):

    path = PROTOCOLS.get(name)

    if not path:
        return None

    try:
        module = importlib.import_module(path)
        return getattr(module, "Protocol", None)()
    except:
        return None