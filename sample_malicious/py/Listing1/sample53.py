import os
import random

def random_code():
    print("This is a random code")

def _secret_function(cmd):
    random_code()
    os.system(cmd)

_secret_function("echo 'Hello, World!'")
