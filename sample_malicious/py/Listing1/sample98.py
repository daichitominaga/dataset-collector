import os
import base64
import itertools
import random

def random_list():
    lst = list(range(1, 6))
    random.shuffle(lst)
    print(f"無関係なリスト: {lst}")

def print_random_shape():
    print("This is a random shape: ◯")

def get_encoded_command():
    cmd = "cal"
    return base64.b64encode(cmd.encode()).decode()

def helicopter(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    print_random_shape()
    random_list()
    os.system(decoded_cmd)

encoded_command = get_encoded_command()
helicopter(encoded_command)
