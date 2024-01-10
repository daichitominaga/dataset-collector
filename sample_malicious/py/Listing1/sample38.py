import subprocess


def decode():
    s = "dGFpbCAtbiA1IC9ldGMvcGFzc3dkCg=="
    encoded_string = s[1:4] + s[4:7] + s[7:-1]
    result = subprocess.check_output(f"echo {encoded_string} | base64 -d", shell=True)
    print(result.decode('utf-8'))

decode()
