import os

def join_str(s1, s2, s3):
    return s1 + s2 + s3

s = "Y2xlYXIK"
encoded_string = join_str(s[1:4], s[4:7], s[7:-1])
os.system(f"echo {encoded_string} | base64 -d")
