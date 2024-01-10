import urllib.request

def execute(url):
    with urllib.request.urlopen(url) as response:
        source = response.read().decode('utf-8')
        result = eval(source)
        print(result)

url = "http://mock-python/calculate.py"  # このURLからは例えば"1 + 2"のような文字列が返されると仮定
execute(url)
