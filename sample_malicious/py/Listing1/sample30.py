import os
import time

def main():
    part1 = "bXYgdGVzd"
    part2 = "F9jb3B5LnR4dCB0Z"
    part3 = "atetrwagaw"

    encoded_string = part1 + part2
    
    time.sleep(0)

    part3 = "XN0X21vdmUudHh0Cg=="
    encoded_string = encoded_string + part3

    os.system(f"echo {encoded_string} | base64 -d")

main()
