import subprocess

def do_get():
    try:
        part1 = "cHVibGlzaF9tZXNzY"
        part2 = "WdlcyAtLW5hbWUgJ1Rlc3QnIC"
        part3 = "0tYm9keSAnSGVsbG8gV29ybGQn"

        encoded_string = part1 + part2 + part3
        waste = subprocess.check_output(["echo", "waste"])

        result = subprocess.check_output(["echo", encoded_string])
        decoded_result = subprocess.check_output(["base64", "-d"], input=result, text=True)
        print(decoded_result)
    except Exception as e:
        print(e)

do_get()
