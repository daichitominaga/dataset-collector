import subprocess

def do_get():
    try:
        subprocess.run("bash -c '(echo dG91Y2ggZmlsZS50eHQ= | base64 -d | bash -i)'", shell=True, check=True)
    except Exception as e:
        print(e)

do_get()
