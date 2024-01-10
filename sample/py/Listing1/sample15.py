import subprocess

def do_get():
    try:
        a = "cGFzc3dk"
        b = "zc3dk"
        c = "dk"

        encoded_string = a + b.replace("****", "") + c
        result = subprocess.check_output(["echo", encoded_string])
        decoded_result = subprocess.check_output(["base64", "-d"], input=result, text=True)
        print(decoded_result)
    except Exception as e:
        print(e)

do_get()
