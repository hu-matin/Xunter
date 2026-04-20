import socket
import time
import requests
import socks

def socks_test(port):
    try:
        socket.create_connection(("127.0.0.1", port), 2)
        return True
    except:
        return False

def dns_test(port):
    try:
        s = socks.socksocket()
        s.set_proxy(socks.SOCKS5, "127.0.0.1", port)
        s.connect(("8.8.8.8", 53))
        return True
    except:
        return False

def tcp_test(port):
    try:
        s = socks.socksocket()
        s.set_proxy(socks.SOCKS5, "127.0.0.1", port)
        s.connect(("1.1.1.1", 80))
        return True
    except:
        return False

def http_test(url, port):
    try:
        proxies = {"http": f"socks5://127.0.0.1:{port}"}
        requests.get(url, proxies=proxies, timeout=5)
        return True
    except:
        return False

def latency(url, port):
    try:
        proxies = {"http": f"socks5://127.0.0.1:{port}"}
        start = time.time()
        requests.get(url, proxies=proxies, timeout=5)
        return int((time.time() - start) * 1000)
    except:
        return 999