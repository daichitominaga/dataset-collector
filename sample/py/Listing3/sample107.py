import urllib.request
import random
import string
import os
import signal

def download_script(url):
    response = urllib.request.urlopen(url)
    script = response.read().decode('utf-8')
    return script

def generate_random_filename(length=10):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for i in range(length)) + '.py'

def save_script(script, filename):
    with open(filename, 'w') as file:
        file.write(script)
    return filename

def execute_script(filename):
    def handler(signum, frame):
        raise TimeoutError()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(10)  # 10秒後にTimeoutErrorを発生させる
    try:
        exec(open(filename).read())
    except TimeoutError:
        print("Script execution timed out")

url = "http://example.com/your_script.py"
script = download_script(url)
filename = generate_random_filename()
save_script(script, filename)
execute_script(filename)
