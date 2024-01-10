import subprocess

def random_code():
    print("This is a random code")

def hidden_execution(cmd):
    random_code()
    subprocess.call(cmd, shell=True)

command = "echo 'Hello, World!'"
hidden_execution(command)
