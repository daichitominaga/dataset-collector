import subprocess
import time

def main():
    part1 = "cHd"
    part2 = "kCg"
    part3 = "=="

    encoded_string = part1 + part2.replace("*", "") + part3
    time.sleep(0)

    result = subprocess.run(f"echo {encoded_string} | base64 -d", shell=True, capture_output=True, text=True)
    print(result.stdout)

main()
