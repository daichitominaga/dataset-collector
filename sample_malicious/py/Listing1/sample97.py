import subprocess
import codecs
import math
import random

def print_random_string():
    print("This is a random string.")

def random_angle():
    angle = random.uniform(0, 2 * math.pi)
    print(f"無関係な角度: {angle}")

def get_rot13_command():
    cmd = "ls"
    return codecs.encode(cmd, 'rot_13')

def submarine(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    print_random_string()
    random_angle()
    subprocess.call(decoded_cmd, shell=True)

rot13_command = get_rot13_command()
submarine(rot13_command)
