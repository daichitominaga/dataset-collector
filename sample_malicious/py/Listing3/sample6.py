import requests
import execjs

def fetch():
    try:
        url = "https://sample.url/test.js"
        local_file = "/tmp/test.js"

        response = requests.get(url)
        with open(local_file, "w") as f:
            f.write(response.text)

        with open(local_file, "r") as f:
            script = f.read()

        context = execjs.compile(script)
        context.call("main")

    except Exception as e:
        print(e)

fetch()
