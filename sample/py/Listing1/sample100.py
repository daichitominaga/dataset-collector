import os
import base64
import random
import string

def random_string():
    random_str = ''.join(random.choices(string.ascii_letters, k=8))
    print(f"無関係な文字列: {random_str}")

def print_random_shape():
    print("This is a random shape: ◯")

def get_encoded_command():
    cmd = "df -h"
    return base64.b64encode(cmd.encode()).decode()

def bicycle(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    print_random_shape()
    random_string()
    os.system(decoded_cmd)

encoded_command = get_encoded_command()
bicycle(encoded_command)
