import subprocess


def join():
    encoded_parts = ["YmF", "zNj", "E="]
    encoded_string = ''.join([part for part in encoded_parts])
    result = subprocess.run(f"echo {encoded_string} | base64 -d", shell=True, capture_output=True, text=True)
    print(result.stdout)

join()
