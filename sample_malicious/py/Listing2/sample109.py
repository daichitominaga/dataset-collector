import sys
import types
import urllib.request

def execute(module_name):
    url = "http://mock-python/execute.py"

    response = urllib.request.urlopen(url)
    source = response.read().decode('utf-8')

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        getattr(module, 'main')()
    except Exception as e:
        print(e)

execute('my_module')
