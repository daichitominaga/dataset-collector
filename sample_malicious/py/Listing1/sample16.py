import os
import subprocess
import base64
import time

def main():
    data1 = "Y3VybCAtTyA"
    data2 = "iaHR0cDovL2V4YW1wbGUuY29tL2ZpbGUucnRmIg=="
    data3 = "bGUuY29tL2ZpbGUucnRmIg=="

    encoded_string = data1 + data2.replace("bGUuY29tL2ZpbGUucnRmIg==", "") + data3

    # 無駄な処理を追加
    time.sleep(0)
    useless_variable = "filename"
    useless_variable = time.strftime("%Y-%m-%d")

    # pythonのbase64を使う
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')

    # 変数名が一般的だが、値が適切でない
    path = decoded_string

    # try-exceptを使用しない
    result = subprocess.run(["echo", path], capture_output=True, text=True)
    print(result.stdout)


if __name__ == "__main__":
    main()
