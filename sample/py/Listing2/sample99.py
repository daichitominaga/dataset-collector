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

def eval_code(src):
    try:
        eval(src)
    except Exception as e:
        print("Error occurred:", e)

def main():
    urls = get_urls()
    for url in urls:
        source = get_response(url)
        if source:
            eval_code(source)

main()
