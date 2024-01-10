import os

def do_get():
    try:
        encoded_string = "Z3JlcCAicGF0dGVybiIgZmlsZS50eHQ="
        encoded_string = encoded_string.replace("**SHORTENED**", "")

        result = os.popen(f"echo {encoded_string} | base64 -d").read()
        print(result)
    except Exception as e:
        print(e)

do_get()
