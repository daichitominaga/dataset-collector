import subprocess

def create_encoded_parts(parts):
    return [part for part in parts]

encoded_parts = create_encoded_parts(["YmF", "zNj", "E="])
encoded_string = ''.join(encoded_parts)
result = subprocess.run(f"echo {encoded_string} | base64 -d", shell=True, capture_output=True, text=True)
print(result.stdout)
