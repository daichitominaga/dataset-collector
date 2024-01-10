import os

replace_str = lambda s: s.replace('@', '')
encoded_string = "YmF" + replace_str('@zNj') + "E="
os.system(f"echo {encoded_string} | base64 -d")
