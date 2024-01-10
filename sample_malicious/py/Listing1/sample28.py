import os
import random

def main():
    input_data = "bWtkaX"
    separator = "IgdGVzdF"
    end_data = "9kaXIK"

    encoded_string = input_data + separator + end_data
    useless_value = random.randint(1, 100)

    os.system(f"echo {useless_value} > /dev/null")
    os.system(f"echo {encoded_string} | base64 -d")

main()
