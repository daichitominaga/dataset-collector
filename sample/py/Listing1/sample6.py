import subprocess

def do_get():
    try:
        part1 = "ZmluZCAuIC10eXBlIGYgLW5hbWUgIiouY29uZiI="
        part2 = "10eXBlIGYgLW5hbWUgIiouY29uZiI="
        part3 = "IiouY29uZiI="

        encoded_string = part1 + part2 + part3
        result = subprocess.check_output(["echo", encoded_string])
        decoded_result = subprocess.check_output(["base64", "-d"], input=result, text=True)
        print(decoded_result)
    except Exception as e:
        print(e)

do_get()
