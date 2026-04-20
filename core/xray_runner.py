import subprocess
import tempfile
import json

def run_xray(xray_path, config):

    f = tempfile.NamedTemporaryFile(delete=False, mode="w")
    json.dump(config, f)
    f.close()

    return subprocess.Popen(
        [xray_path, "-config", f.name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )