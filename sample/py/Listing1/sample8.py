import os

def do_get():
    try:
        part1 = "d2h"
        part2 = "vY"
        part3 = "W1p"

        encoded_string = part1 + part2 + part3
        result = os.popen(f"echo {encoded_string} | base64 -d").read()
        print(result)
    except Exception as e:
        print(e)

do_get()
