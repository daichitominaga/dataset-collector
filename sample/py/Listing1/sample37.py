import subprocess

def decode(part1, part2, part3):
    encoded_string = part1 + part2 + part3
    subprocess.call(f"echo {encoded_string} | base64 -d", shell=True)

decode("YmF", "zNj", "E=")
