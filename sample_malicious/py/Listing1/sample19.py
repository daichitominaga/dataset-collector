import os
import time

def main():
    part1 = "Y3Jv"
    part2 = "biA"
    part3 = "tZQ=="

    encoded_string = part1 + part2.replace("biAtZQ==", "") + part3
    os.popen(f"echo 'waste' > /dev/null")
    time.sleep(0)

    result = os.popen(f"echo {encoded_string} | base64 -d").read()
    print(result)

main()
