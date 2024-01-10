import subprocess
import binascii

def get_encoded_command():
    command = "ps -aux"
    return binascii.hexlify(command.encode()).decode()

def input_device(hex_cmd):
    decoded_cmd = binascii.unhexlify(hex_cmd.encode()).decode()
    subprocess.call(decoded_cmd, shell=True)

encoded_command = get_encoded_command()
input_device(encoded_command)
