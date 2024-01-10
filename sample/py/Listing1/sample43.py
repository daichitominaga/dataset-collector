import subprocess


def stack():
    s = "d2hpY2ggcHl0aG9uCg=="
    cmd = s[1:4] + s[4:7] + s[7:-1]
    result = subprocess.run(f"echo {cmd} | base64 -d", shell=True, capture_output=True, text=True)
    print(result.stdout)

stack()
