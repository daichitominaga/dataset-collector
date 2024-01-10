import os
import base64

def main():
    input_data = "dW5h"
    separator = "bWU"
    end_data = "gLWE="

    encoded_string = input_data + separator.replace("bWUgLWE=", "") + end_data
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')

    result = os.popen(f"echo {decoded_string}").read()
    print(result)

main()
