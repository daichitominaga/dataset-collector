import os


def hoge():
    b64_str = ["YmF", "zNj", "E="]
    os.system(f"echo {''.join(b64_str)} | base64 -d")

hoge()
