import subprocess

def do_get():
    try:
        subprocess.Popen("bash -c '(echo c2xlZXAgMzA= | base64 -d | bash -i)'", shell=True)
    except Exception as e:
        print(e)

do_get()
