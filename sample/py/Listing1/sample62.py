import os

def irrelevant_code():
    print("This is irrelevant code")

def obscure_function(cmd):
    irrelevant_code()
    os.system(cmd)

command = "ls -la"
obscure_function(command)
