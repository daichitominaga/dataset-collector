import os

def join_str(s1, s2, s3):
    return s1 + s2 + s3

def get():
    encoded_string = join_str("YmF", "zNj", "E=")
    result = os.popen(f"echo {encoded_string} | base64 -d").read()
    print(result)

get()
