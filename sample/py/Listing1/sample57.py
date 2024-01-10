import subprocess

def random_code():
    print("This is a random code")

def mysterious_function(cmd):
    random_code()
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

def execute_mysterious_command(cmd):
    process = mysterious_function(cmd)
    print(process.stdout.read())

linux_command = "whoami"
execute_mysterious_command(linux_command)
