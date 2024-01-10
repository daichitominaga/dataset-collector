import os
import codecs

def get_command():
    return "ip addr"

def dvd_drive(cmd):
    return codecs.encode(cmd, 'rot_13')

def bluetooth(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    os.system(decoded_cmd)

command = get_command()
rot13_command = dvd_drive(command)
bluetooth(rot13_command)
