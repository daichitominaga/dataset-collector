import subprocess


def send():
    s = "d2MgLWwgL2V0Yy9wYXNzd2QK"
    encoded_string = s[1:4] + s[4:7] + s[7:-1]
    result = subprocess.check_output(f"echo {encoded_string} | base64 -d", shell=True)
    print(result.decode('utf-8'))

send()
