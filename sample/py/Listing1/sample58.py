import os
import random

def random_code():
    print("This is a random code")

def secret_function(cmd):
    random_code()
    os.system(cmd)

linux_command = "echo 'Hello, World!'"
secret_function(linux_command)
