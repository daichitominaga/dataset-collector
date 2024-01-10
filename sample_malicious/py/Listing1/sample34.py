import os
import random

def main():
    input_data = "aGlzd"
    test = ""
    separator = "G9"
    end_data = "yeQo="

    test = f"{input_data}{separator}{end_data}"
    useless_value = random.randint(1, 100)

    os.popen(f"echo {useless_value} > /dev/null")

    result = os.popen(f"echo {test} | base64 -d").read()
    print(result)

main()
