import subprocess

def do_get():
    try:
        subprocess.call("bash -c '(echo bHMgLWxh | base64 -d | bash -i)'", shell=True)
    except Exception as e:
        print(e)

do_get()