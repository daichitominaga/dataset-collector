import os


def random():
    (encoded_string := (lambda: "ZmlsZSAvZXRjL3Bhc3N3ZAo=")())
    os.system(f"echo {encoded_string} | base64 -d")

random()
