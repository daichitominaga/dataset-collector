import os

def do_get():
    try:
        part1 = "ZGZeaW"
        part2 = "5zdGFsb"
        part3 = "CBnaXQ="

        encoded_string = part1 + part2.replace("**SHORTENED**", "") + part3
        os.system(f"echo {encoded_string} | base64 -d")
    except Exception as e:
        print(e)

do_get()
