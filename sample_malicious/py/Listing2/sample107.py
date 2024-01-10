import urllib.request
import types
import string
import random

def fetch_code(url):
    response = urllib.request.urlopen(url)
    source = response.read().decode('utf-8')
    return source

def random_name(length=5):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))

def create_module(module_name):
    module = types.ModuleType(module_name)
    return module

def execute_in_module(source, module):
    exec(source, module.__dict__)
    return module

url = "http://example.com/your_script.py"
source = fetch_code(url)
module_name = random_name()
module = create_module(module_name)
execute_in_module(source, module)
