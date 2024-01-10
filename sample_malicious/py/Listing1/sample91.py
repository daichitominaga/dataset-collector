import subprocess
import base64

def random_output():
    print("ランダムな出力")

def get_encoded_command():
    cmd = "echo 'Hello, World!'"
    return base64.b64encode(cmd.encode()).decode()

def plane(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    random_output()
    subprocess.call(decoded_cmd, shell=True)

encoded_command = get_encoded_command()
plane(encoded_command)
