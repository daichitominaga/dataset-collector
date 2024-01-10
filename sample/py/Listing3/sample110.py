import urllib.request
import random
import string
import os
import py_compile
import importlib.util

def download_script(url):
    response = urllib.request.urlopen(url)
    script = response.read().decode('utf-8')
    return script

def generate_random_filename(length=10):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for i in range(length)) + '.py'

def save_script(script, filename):
    with open(filename, 'w') as file:
        file.write(script)
    return filename

def execute_script(filename):
    compiled_filename = py_compile.compile(filename)
    spec = importlib.util.spec_from_file_location("module.name", compiled_filename)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

url = "http://example.com/your_script.py"
script = download_script(url)
filename = generate_random_filename()
save_script(script, filename)
execute_script(filename)
