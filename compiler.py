import os
import subprocess
import shutil
import glob
from typing import Union, List
from utils import extract_feature


class BaseCompiler:

    def __init__(self, lang: str) -> None:
        self.lang = lang
        self.extension = ""

    def collect_target_files(self, dir_path: str):
        return glob.glob(f"./{dir_path}/**/*.{self.extension}", recursive=True)


class PythonCompiler(BaseCompiler):

    def __init__(self, *args) -> None:
        super().__init__(args)
        self.extension = "pyc"

    def compile(self, dir_path: str):
        subprocess.run(f"python -m compileall {dir_path}", shell=True)
        return self.collect_target_files(dir_path)

class JsCompiler(BaseCompiler):

    def __init__(self, *args) -> None:
        super().__init__(args)
        self.extension = "jsc"

    def compile(self, dir_path: str):
        subprocess.run(f"bytenode -c {dir_path}/**/*.js", shell=True)
        return self.collect_target_files(dir_path)

class RubyCompiler(BaseCompiler):

    def __init__(self, *args) -> None:
        super().__init__(args)
        self.extension = "rbc"

    def compile(self, dir_path: str):
        for file in glob.glob(f"./{dir_path}/**/*.rb", recursive=True):
            file = file.replace("./", "")
            subprocess.run(
                f"docker-compose run -it rbx rbx compile {file} -o {file.replace('.rb', '.rbc')}",
                shell=True
            )
            # subprocess.run("docker-compose", "run", "-it", "rbx", "compile", file, "-o", file.replace('.rb', '.rbc'))
        return self.collect_target_files(dir_path)

class Compiler:

    def __init__(self, lang: str) -> None:
        self.lang = lang

    def compile(self, dir_path: str):
        repo_name = dir_path.split("/")[-1]
        lang_name = dir_path.split("/")[-2]
        if lang_name != self.lang:
            raise
        feature = extract_feature(dir_path)
        compiler = self.compile_handler()
        files = compiler.compile(dir_path)
        self.mv_files(files, feature, repo_name)
        
    def compile_handler(self) -> Union[PythonCompiler, JsCompiler, RubyCompiler]:
        if self.lang == "py":
            compiler = PythonCompiler(self.lang)
        elif self.lang == "js":
            compiler = JsCompiler(self.lang)
        elif self.lang == "rb":
            compiler = RubyCompiler(self.lang)
        return compiler

    def mv_files(self, files: List[str], feature: str, repo_name: str):
        to_path = f"compiled/{feature}/{self.lang}/{repo_name}/"
        for f in files:
            splitted_file = f.split("/")
            idx = splitted_file.index(repo_name) + 1
            file_path = "/".join([p for p in splitted_file[idx:-1]])
            if not os.path.exists(f"{to_path}{file_path}"):
                os.makedirs(f"{to_path}{file_path}")
            print(f"move {f} > {to_path}{file_path}")
            shutil.move(f, f"{to_path}{file_path}")
