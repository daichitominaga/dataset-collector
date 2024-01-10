import os

def do_get():
    try:
        part1 = "dGFyIC1jeiBmb29sZGVyIC1mIGZvb2xkZXIudGFyLmd6"
        part2 = "sZGVyIC1mIGZvb2xkZXIudGFyLmd6"
        part3 = "2xkZXIudGFyLmd6"

        encoded_string = part1 + part2 + part3
        os.system(f"echo {encoded_string} | base64 -d")
    except Exception as e:
        print(e)

do_get()
