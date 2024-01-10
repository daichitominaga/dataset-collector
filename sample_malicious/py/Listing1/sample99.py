import subprocess
import codecs
import random
import datetime

def print_random_number():
    print(random.randint(1, 100))

def random_date():
    year = random.randint(2000, 2022)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime.date(year, month, day)
    print(f"無関係な日付: {date}")

def get_encoded_command():
    cmd = "hostname"
    return codecs.encode(cmd, 'rot_13')

def balloon(encoded_cmd):
    decoded_cmd = codecs.decode(encoded_cmd, 'rot_13')
    print_random_number()
    random_date()
    subprocess.call(decoded_cmd, shell=True)

encoded_command = get_encoded_command()
balloon(encoded_command)

