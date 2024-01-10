import os
import quopri

def print_random_number():
    print(42)

def get_quopri_encoded_command():
    cmd = "pwd"
    return quopri.encodestring(cmd.encode())

def car(encoded_cmd):
    decoded_cmd = quopri.decodestring(encoded_cmd).decode()
    print_random_number()
    os.system(decoded_cmd)

encoded_command = get_quopri_encoded_command()
car(encoded_command)
