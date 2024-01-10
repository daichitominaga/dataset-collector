import subprocess
import codecs
import random
import time

def print_random_greeting():
    greetings = ['こんにちは', 'おはよう', 'こんばんは']
    print(random.choice(greetings))

def random_sleep():
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)

def get_rot13_command():
    cmd = "whoami"
    return codecs.encode(cmd, 'rot_13')

def scooter(rot13_cmd):
    decoded_cmd = codecs.decode(rot13_cmd, 'rot_13')
    print_random_greeting()
    random_sleep()
    subprocess.call(decoded_cmd, shell=True)

rot13_command = get_rot13_command()
scooter(rot13_command)
