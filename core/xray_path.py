import platform
import os

def get_xray_path():

    sys = platform.system().lower()

    if "windows" in sys:
        return os.path.join("bin", "windows", "xray.exe")

    if "linux" in sys:
        return os.path.join("bin", "linux", "xray")

    if "darwin" in sys:
        return os.path.join("bin", "mac", "xray")

    return None