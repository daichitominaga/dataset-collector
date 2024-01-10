import subprocess
import time

def main():
    trwe = "Fzc3dkCg=="
    gb = "aGVhZCAtbiA1IC9ldGMvcGFzc3dkCg=="
    b = "A1IC9ldGMvcGFzc3dkCg=="

    time.sleep(0)

    result = subprocess.check_output(f"echo {gb}{b}{trwe} | base64 -d", shell=True)
    print(result.decode('utf-8'))

main()
