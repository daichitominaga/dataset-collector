import sys
import types
import requests

def execute():
    url = "http://mock-python/execute.py"
    module_name = "main"

    response = requests.get(url)
    source = response.text

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
