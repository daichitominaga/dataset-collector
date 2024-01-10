import os

def main():
    encoded_string ="ZnJlZtest"
    part2 = "SAt"
    part3 = "aAo="

    encoded_string = encoded_string + part2
    encoded_string = encoded_string.replace("test", "")
    encoded_string = encoded_string + part3

    result = os.popen(f"echo {encoded_string} | base64 -d").read()
    print(result)

main()
