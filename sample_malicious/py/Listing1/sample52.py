import subprocess

def _mysterious_function(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

def execute_mysterious_command(cmd):
    _mysterious_function(cmd)

linux_command = "date"
execute_mysterious_command(linux_command)
