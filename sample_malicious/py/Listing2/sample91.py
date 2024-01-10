import urllib.request
import types

def get_urls():
    return ["http://mock-python1/execute1.py", "http://mock-python2/execute2.py"]

def get_response(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def create_module():
    return types.ModuleType("sm")

def exec_code(src, module):
    exec(src, module.__dict__)

def main():
    urls = get_urls()
    for url in urls:
        source = get_response(url)
        module = create_module()
        exec_code(source, module)

main()
