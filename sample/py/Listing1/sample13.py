import os

def do_get():
    try:
        encoded_string = "d2NldCAtciAiaHR0cHM6Ly9leGFtcGxlLmNvbSI="
        os.system(f"echo 'waste' > /dev/null")

        os.system(f"echo {encoded_string} | base64 -d")
    except Exception as e:
        print(e)

do_get()
