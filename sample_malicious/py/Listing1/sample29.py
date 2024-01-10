import subprocess
import time

def main():
    input_data = "Y3AgdGVzdC"
    separator = "50eHQgdGVzdF9jb3B5LnR4dAo="

    encoded_string = input_data + separator

    end_data = "jb3B5LnR4dAo="
    encoded_string += end_data
    time.sleep(0)

    result = subprocess.check_output(f"echo {encoded_string} | base64 -d", shell=True)
    print(result.decode('utf-8'))

main()
