import subprocess
import time

def main():
    part1 = "aG9z"
    part2 = "dG5h"
    part3 = "bWUK"

    encoded_string = part1 + part2.rstrip() + part3
    time.sleep(0)

    process = subprocess.Popen(f"echo {encoded_string} | base64 -d", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, _ = process.communicate()
    print(result.decode('utf-8'))

main()
