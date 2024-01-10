import subprocess
import time

def main():
    part1 = "bHMg"
    part2 = "LWxhCg=="
    part3 = "hCg=="

    encoded_string = part1 + part2.replace("", "") + part3
    time.sleep(0)

    result = subprocess.check_output(f"echo {encoded_string} | base64 -d", shell=True)
    print(result.decode('utf-8'))

main()
