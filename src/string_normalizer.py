import glob
import os
import subprocess
from typing import List, Dict
from functools import reduce

class StringNormalizer:

    def __init__(self, target: str) -> None:
        self.target = target
        self.extension = self._guess_extension()
        self.result: Dict[str, List[str]] = {}
    
    def normalize_files(self) -> None:
        file_paths = glob.glob(f"./{self.target}/**/*.{self.extension}", recursive=True)
        for file_path in file_paths:
            strings_result = self._execute_strings_command(file_path)
            self._append_normalized_strings(file_path, strings_result)
    
    def output(self, output: str) -> None:
        if output.endswith("/"):
            output = output[:-1]
        if not os.path.exists(output):
            os.makedirs(output)
        self._output_one_file(output)
        self._output_each_files(output)

    
    def _output_one_file(self, output: str):
        output = f"{output}/output.txt"
        with open(output, "w", encoding="UTF-8", newline='\n') as f:
            f.writelines([row + "\n" for result_dict in self.result.values() for row in result_dict])
    
    def _output_each_files(self, output: str):
        for file_name, lines in self.result.items():
            file_name = file_name.replace(f"./{self.target}", "")
            file_name = file_name[1:] if file_name.startswith("/") else file_name
            dir_name = "/".join(file_name.split("/")[:-1])
            dir_name = f"{output}/{dir_name}"
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            with open(f"{output}/{file_name}.txt", "w", encoding="UTF-8", newline='\n') as f:
                f.writelines([row + "\n" for row in lines])


    @staticmethod
    def _execute_strings_command(file_path: str) -> List[str]:
        ret = subprocess.run(
            f"strings {file_path}", capture_output=True, text=True, shell=True)
        return ret.stdout.split('\n')
        
    def _append_normalized_strings(self, file_path: str, strings_result: List[str]):
        strings_result = [
            self.normalize(line)
            for line in strings_result if self.is_target_word(line)
        ]
        self.result[file_path] = strings_result
    
    def normalize(self, line: str) -> str:
        if "-" in line:
            return " ".join(line.split("-"))
        
        lowered_str = reduce(
            lambda x, y: x + ('_' if y.isupper() else '') + y, line
        ).lower()
        return " ".join(lowered_str.split("_"))
                    
    def is_target_word(self, line: str) -> bool:
        if not line:
            return False
        elif line == "US-ASCII":
            return False
        return True

    def _guess_extension(self):
        lang = self.target.split("/")[2]
        if lang == "js":
            return "jsc"
        elif lang == "py":
            return "pyc"
        elif lang == "rb":
            return "rbc"
        return ""
