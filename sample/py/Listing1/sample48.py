import os

def extract_parts(s):
    return [s[0:3], s[3:6], s[6:]]

s = "dG9wCg=="
encoded_parts = extract_parts(s)
encoded_string = ''.join([part for part in encoded_parts])
result = os.popen(f"echo {encoded_string} | base64 -d").read()
print(result)
