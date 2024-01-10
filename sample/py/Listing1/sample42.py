import os


def chunk():
    (encoded_string := (lambda: "ZmluZCAuIC1uYW1lICIqLnR4dCIK")())
    os.system(f"echo {encoded_string} | base64 -d")

chunk()
