import os
import uu
import io

def get_command_from_file():
    with open("command.txt", "r") as file:
        return file.read().strip()

def cooling_system(cmd):
    input_io = io.BytesIO(cmd.encode())
    output_io = io.BytesIO()
    uu.encode(input_io, output_io)
    return output_io.getvalue().decode()

def battery(encoded_cmd):
    input_io = io.BytesIO(encoded_cmd.encode())
    output_io = io.BytesIO()
    uu.decode(input_io, output_io)
    decoded_cmd = output_io.getvalue().decode()
    os.system(decoded_cmd)

command = get_command_from_file()
encoded_command = cooling_system(command)
battery(encoded_command)
