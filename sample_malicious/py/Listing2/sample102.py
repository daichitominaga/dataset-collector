import urllib.request

def execute(url):
    response = urllib.request.urlopen(url):
    source = response.read().decode('utf-8')
    exec(source)

url = "http://mock-python/calculate.py"  # このURLからは例えば"result = 1 + 2"のような文字列が返されると仮定
execute(url)
print(result)  # ここで出力されるresultはexecによって計算された結果
