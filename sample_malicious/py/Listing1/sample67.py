import os
import uu
import io

def uuencode_command(cmd):
    input_io = io.BytesIO(cmd.encode())
    output_io = io.BytesIO()
    uu.encode(input_io, output_io)
    return output_io.getvalue().decode()

def uudecode_execute_command(encoded_cmd):
    input_io = io.BytesIO(encoded_cmd.encode())
    output_io = io.BytesIO()
    uu.decode(input_io, output_io)
    decoded_cmd = output_io.getvalue().decode()
    os.system(decoded_cmd)

command = "hostname"
encoded_command = uuencode_command(command)
uudecode_execute_command(encoded_command)
