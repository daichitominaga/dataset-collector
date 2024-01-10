import os
import binascii

def obscure_command(cmd):
    return binascii.hexlify(cmd.encode()).decode()

def execute_obscure_command(hex_cmd):
    decoded_cmd = binascii.unhexlify(hex_cmd.encode()).decode()
    os.system(decoded_cmd)

command = "uname -a"
hex_command = obscure_command(command)
execute_obscure_command(hex_command)
