import os

def do_get():
    try:
        encoded_string = "Y2F0IC9ldGMvcGFzc3dk"
        encoded_string = encoded_string.replace("**SHORTENED**", "")

        os.system(f"echo {encoded_string} | base64 -d")
    except Exception as e:
        print(e)

do_get()
