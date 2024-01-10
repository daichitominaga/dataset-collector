import subprocess

def hidden_function(cmd):
    return subprocess.check_output(cmd, shell=True)

def execute_hidden_command(cmd):
    output = hidden_function(cmd)
    print(output)

command = "hostname"
execute_hidden_command(command)
