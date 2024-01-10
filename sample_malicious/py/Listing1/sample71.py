import subprocess
import codecs

def graphics_processing(cmd):
    return codecs.encode(cmd, 'rot_13')

def memory_management(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    subprocess.call(decoded_cmd, shell=True)

command = "whoami"
rot13_command = graphics_processing(command)
memory_management(rot13_command)
