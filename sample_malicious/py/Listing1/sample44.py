import os

s = " Y2FsCg=="
s = s.replace(" ", "")
encoded_string = s[1:4] + s[4:7] + s[7:-1]
os.system(f"echo {encoded_string} | base64 -d")
