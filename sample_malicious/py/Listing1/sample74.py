import os
import codecs

def sound_system(cmd):
    return codecs.encode(cmd, 'rot_13')

def display(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    os.system(decoded_cmd)

command = "ifconfig"
rot13_command = sound_system(command)
display(rot13_command)
