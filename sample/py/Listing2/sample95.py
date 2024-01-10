import urllib.request
import importlib

def get_urls():
    return ["http://mock-python1/execute1.py", "http://mock-python2/execute2.py"]

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def exec_code(src):
    exec(src)

def main():
    urls = get_urls()
    for url in urls:
        source = get_response(url)
        exec_code(source)

main()
