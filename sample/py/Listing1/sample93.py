import subprocess
import uu

def useless_output():
    print("This output is useless.")

def generate_uuencoded_command():
    cmd = "date"
    return uu.encode(input=cmd.encode(), output=None)

def boat(encoded_cmd):
    decoded_cmd = uu.decode(input=encoded_cmd, output=None)
    useless_output()
    subprocess.call(decoded_cmd, shell=True)

encoded_command = generate_uuencoded_command()
boat(encoded_command)
