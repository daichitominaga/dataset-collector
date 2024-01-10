import sys
import types
import requests

def get_url_and_module_name():
    return "http://downloads.example.org/scripts/app_config.py", "config"

def execute():
    url, module_name = get_url_and_module_name()
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
