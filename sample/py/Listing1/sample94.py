import subprocess
import codecs

def print_random_shape():
    print("This is a random shape: ◯")

def get_encoded_command():
    cmd = "cal"
    return codecs.encode(cmd, 'rot_13')

def kite(encoded_cmd):
    decoded_cmd = codecs.decode(encoded_cmd, 'rot_13')
    print_random_shape()
    subprocess.call(decoded_cmd, shell=True)

encoded_command = get_encoded_command()
kite(encoded_command)
