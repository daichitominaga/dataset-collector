import os
import random
import shutil
import glob
from pathlib import Path

malicious_code_file_path = "malicious_code/py"
target_directory = "/Volumes/WD_BLACK/repositories/various/py"
destination_directory = "embedd_malicious_codes/py"

def collect_files(dir_path: str, extension: str):
    return glob.glob(f"{dir_path}/**/*.{extension}", recursive=True)

def load_malicious_code(file_path: str):
    with open(file_path, "r") as malicious_code_file:
        return malicious_code_file.read()

def select_file_path(python_files: list[Path], embed_table: list[dict]):
    embedded_file_names = [t["original_source"].split("/")[-1] for t in embed_table] if embed_table else []
    while True:
        selected_file_path = random.choice(python_files)
        if str(selected_file_path).split("/")[-1] in embedded_file_names:
            continue
        if "test" in str(selected_file_path):
            continue
        if "migrations" in str(selected_file_path):
            continue
        return selected_file_path

def main():
    malicious_files = collect_files(malicious_code_file_path, "py")
    python_files = list(Path(target_directory).glob('**/*.py'))
    embed_table= []
    for malicious_file in malicious_files:
        content = load_malicious_code(malicious_file)
        selected_file_path = select_file_path(python_files, embed_table)
        destination_file_path = os.path.join(destination_directory, os.path.basename(selected_file_path))
        shutil.copy(selected_file_path, destination_file_path)
        with open(destination_file_path, "a") as destination_file:
            destination_file.write("\n" + content)
        embed_table.append(
            {
                "original_source": str(selected_file_path),
                "embedded_source": malicious_file,
            }
        )
        print(f"書き込み完了: {destination_file_path}, {malicious_file}")
