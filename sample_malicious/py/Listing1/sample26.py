import subprocess
import time

def main():
    input_data = "ZGYg"
    separator = "LWgK"
    end_data = "gK"

    encoded_string = input_data + separator + end_data
    time.sleep(0)

    subprocess.call(f"echo {encoded_string} | base64 -d", shell=True)

main()
