import sys
import types
import requests

def get_url():
    return "http://media.medialib.jp/python/core_module.py"

def get_module_name():
    return "core"

def foo(url, module_name):
    response = requests.get(url)
    source = response.text

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)

    return module

def main():
    url = get_url()
    module_name = get_module_name()

    module = foo(url, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

main()
