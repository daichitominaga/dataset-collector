import os
import time

def main():
    input_data = "dW5h"
    separator = "bWUgLWEK"
    end_data = "LWEK"

    encoded_string = input_data + separator + end_data
    os.popen(f"echo 'waste' > /dev/null")
    time.sleep(0)

    result = os.popen(f"echo {encoded_string} | base64 -d").read()
    print(result)

main()
