import urllib.request
import os

def execute(url):
    with urllib.request.urlopen(url) as response:
        script_path = response.read().decode('utf-8')
        os.system(f"./{script_path}")

url = "http://mock-python/script_path.exe"  # このURLからはPythonスクリプトへのパスが返されると仮定
execute(url)
