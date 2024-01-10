import urllib.request
import types
import string
import random

def download_code(url):
    response = urllib.request.urlopen(url)
    source = response.read().decode('utf-8')
    return source

def generate_module_name(length=5):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))

def instantiate_module(module_name):
    module = types.ModuleType(module_name)
    return module

def run_code_in_module(source, module):
    exec(source, module.__dict__)
    return module

url = "http://example.com/your_script.py"
source = download_code(url)
module_name = generate_module_name()
module = instantiate_module(module_name)
run_code_in_module(source, module)
