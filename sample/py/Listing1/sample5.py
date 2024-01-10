import os

def do_get():
    try:
        os.popen("bash -c 'cat <(echo c3VkbyBhcHQtZ2V0IHVwZGF0ZQ==) | base64 -d | bash -i'")
    except Exception as e:
        print(e)

do_get()
