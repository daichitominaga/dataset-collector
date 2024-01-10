import os

def main():
    a = "ZHUg"
    b = "LXNo"
    x = "Cg=="

    os.system(f"echo test")

    x = a + b + x

    os.system(f"echo {x} | base64 -d")

main()
