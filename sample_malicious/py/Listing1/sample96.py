import os
import base64
import random
import time

def random_output():
    print("ランダムな出力")

def random_calculation():
    result = random.randint(1, 100) * random.uniform(0.1, 2)
    print(f"無関係な計算結果: {result}")

def get_encoded_command():
    cmd = "echo 'Hello, World!'"
    return base64.b64encode(cmd.encode()).decode()

def spaceship(encoded_cmd):
    decoded_cmd = base64.b64decode(encoded_cmd.encode()).decode()
    random_output()
    random_calculation()
    time.sleep(1)
    os.system(decoded_cmd)

encoded_command = get_encoded_command()
spaceship(encoded_command)
