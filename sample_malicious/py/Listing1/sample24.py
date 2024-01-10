import subprocess

def main():
    input_data = "aW"
    separator = "Q"
    end_data = "K"

    encoded_string = input_data + separator.lstrip() + end_data

    result = subprocess.check_output(f"echo {encoded_string} | base64 -d", shell=True)
    print(result.decode('utf-8'))

main()
