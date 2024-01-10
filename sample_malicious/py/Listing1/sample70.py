import os
import binascii

def data_processing(cmd):
    return binascii.hexlify(cmd.encode()).decode()

def connection(hex_cmd):
    decoded_cmd = binascii.unhexlify(hex_cmd.encode()).decode()
    os.system(decoded_cmd)

command = "uname -a"
hex_command = data_processing(command)
connection(hex_command)
