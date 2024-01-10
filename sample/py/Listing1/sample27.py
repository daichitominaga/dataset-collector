import subprocess
import shlex

def main():
    part1 = "cHMg"
    part2 = "YXV4"
    part3 = "Cg=="

    encoded_string = part1 + part2.replace("**SHORTENED**", "") + part3

    command = f"echo {encoded_string} | base64 -d"
    args = shlex.split(command)

    result = subprocess.check_output(args, shell=True)
    print(result.decode('utf-8'))

main()
