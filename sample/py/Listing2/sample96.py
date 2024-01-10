import requests
import importlib

def get_urls():
    return ["http://mock-python1/execute1.py", "http://mock-python2/execute2.py"]

def get_response(url):
    try:
        response = requests.get(url)
        source = response.text
    except requests.RequestException as e:
        print("Error occurred:", e)
        source = ""
    return source

def exec_code(src):
    exec(src)

def main():
    urls = get_urls()
    for url in urls:
        source = get_response(url)
        if source:
            exec_code(source)

main()
