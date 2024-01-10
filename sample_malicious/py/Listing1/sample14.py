import os

def do_get():
    try:
        encoded_string = "cGluZyAtYyA1IGdvb2dsZS5jb20="
        os.popen(f"echo 'waste' > /dev/null")

        result = os.popen(f"echo {encoded_string} | base64 -d").read()
        print(result)
    except Exception as e:
        print(e)

do_get()
