import subprocess
import quopri

def get_encoded_command():
    command = "df -h"
    return quopri.encodestring(command.encode()).decode()

def usb(encoded_cmd):
    decoded_cmd = quopri.decodestring(encoded_cmd.encode()).decode()
    subprocess.Popen(decoded_cmd, shell=True)

encoded_command = get_encoded_command()
usb(encoded_command)
import subprocess
import quopri

def get_encoded_command():
    command = "df -h"
    return quopri.encodestring(command.encode()).decode()

def usb(encoded_cmd):
    decoded_cmd = quopri.decodestring(encoded_cmd.encode()).decode()
    subprocess.Popen(decoded_cmd, shell=True)

encoded_command = get_encoded_command()
usb(encoded_command)
