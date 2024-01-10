import os
import time

def main():
    str1 = "c3VkbyBhc"
    parsed = "HQtZ2V0IG"
    doc = "luc3RhbGwgYXBhY2hlMg=="

    encoded_string = str1 + parsed.replace("HQtZ2V0IGluc3RhbGwgYXBhY2hlMg==", "") + doc
    os.system(f"echo 'waste' > /dev/null")
    time.sleep(0)

    os.system(f"echo {encoded_string} | base64 -d")

main()
