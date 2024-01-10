import os
import codecs

def obscure_function(cmd):
    return codecs.encode(cmd, 'rot_13')

def execute_obscure_cmd(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    os.system(decoded_cmd)

command = "ifconfig"
rot13_command = obscure_function(command)
execute_obscure_cmd(rot13_command)
