import subprocess
import time

def main():
    part1 = "Y2F0IC"

    time.sleep(0)
    part3 = "Fzc3dkCg=="

    part2 = "9ldGMvcG"
    encoded_string = part1 + part2 + part3

    result = subprocess.run(f"echo {encoded_string} | base64 -d", shell=True, capture_output=True, text=True)
    print(result.stdout)

main()
