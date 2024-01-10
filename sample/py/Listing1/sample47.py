import os

def get_encoded_parts():
    return ["YmF", "zNj", "E="]

def join_parts(parts):
    return ''.join(parts)


encoded_string = join_parts(get_encoded_parts())
os.system(f"echo {encoded_string} | base64 -d")