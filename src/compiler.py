import os
import subprocess
import shutil
import glob
import time
from typing import Union, List
from src.utils import extract_feature


class BaseCompiler:

    def __init__(self, lang: str) -> None:
        self.lang = lang

    def collect_target_files(self, dir_path: str, extension: str = ""):
        return glob.glob(f"./{dir_path}/**/*.{extension}", recursive=True)


class PythonCompiler(BaseCompiler):

    def __init__(self, *args) -> None:
        super().__init__(args)
        # repositories/network/py/simpx-gale/gale/task.pyの
        # print 11111のようなpython2系の構文の場合にエラーがでる。3系で失敗した場合に切り替えるなどの措置が必要
        # exception拾ってとりあえず2系でretryしてみるとかでいいかも

    def compile(self, dir_path: str):
        print(f"execute: python -m compileall {dir_path}")
        subprocess.run(f"python -m compileall {dir_path}", shell=True)
        return self.collect_target_files(dir_path, "pyc")
    
    def print_bytecode(self, dir_path: str):
        for file in glob.glob(f"{dir_path}/**/*.py", recursive=True):
            if "test" in file or os.path.exists(f"{file}.pyc.txt"):
                continue
            file = file.replace("./", "")
            print(f"execute: python -m dis {file} > {file}.pyc.txt")
            subprocess.run(f"python -m dis {file} > {file}.pyc.txt", shell=True)
        return self.collect_target_files(dir_path, "pyc.txt")

class JsCompiler(BaseCompiler):

    def __init__(self, *args) -> None:
        super().__init__(args)

    def compile(self, dir_path: str):
        # js_files = self.collect_target_files(dir_path, "js")
        # for file in js_files:
        #     self.transpile_js(file)
        output_dir = self.transpile_js(dir_path)
        print(f"execute: bytenode -c {output_dir}/**/*.js")
        subprocess.run(f"bytenode -c {output_dir}/**/*.js", shell=True)
        return self.collect_target_files(output_dir, "jsc")
    
    def transpile_js(self, dir_path: str):
        babel = "./node_modules/.bin/babel"
        repo_name = dir_path.split("/")[-1]
        output_dir = f"transpiled/network/js/{repo_name}"
        subprocess.run(
            f"{babel} {dir_path} --out-dir {output_dir}", shell=True)
        return output_dir

class RubyCompiler(BaseCompiler):

    def __init__(self, *args) -> None:
        super().__init__(args)

    def compile(self, dir_path: str):
        for file in glob.glob(f"./{dir_path}/**/*.rb", recursive=True):
            file = file.replace("./", "")
            compile_cmd = f"docker-compose run -it rbx rbx compile {file} -o {file.replace('.rb', '.rbc')}"
            print(f"execute: {compile_cmd}")
            subprocess.run(
                compile_cmd,
                shell=True
            )
            # subprocess.run(
            #     f"docker-compose run -it rbx rbx compile --print-bytecode {file} > file.txt",
            #     shell=True
            # )
            # subprocess.run("docker-compose", "run", "-it", "rbx", "compile", file, "-o", file.replace('.rb', '.rbc'))
        return self.collect_target_files(dir_path, "rbc")

class Compiler:

    def __init__(self, lang: str) -> None:
        self.lang = lang

    def compile(self, dir_path: str, output_path: str = ""):
        repo_name = dir_path.split("/")[-1]
        lang_name = dir_path.split("/")[-2]
        if lang_name != self.lang:
            raise
        feature = extract_feature(dir_path)
        compiler = self.compile_handler()
        files = compiler.compile(dir_path)
        output_path = output_path if output_path else f"compiled/{feature}/{self.lang}/{repo_name}/"
        self.mv_files(output_path, files,  repo_name)

    def print_bytecode(self, dir_path: str, output_path: str = ""):
        repo_name = dir_path.split("/")[-1]
        # lang_name = dir_path.split("/")[-2]
        # if lang_name != self.lang:
        #     raise
        feature = extract_feature(dir_path)
        compiler = self.compile_handler()
        files = compiler.print_bytecode(dir_path)
        time.sleep(5)
        output_path = output_path if output_path else f"print-bytecode/{feature}/{self.lang}/{repo_name}/"
        self.mv_files(output_path, files,  repo_name)
        
    def compile_handler(self) -> Union[PythonCompiler, JsCompiler, RubyCompiler]:
        if self.lang == "py":
            compiler = PythonCompiler(self.lang)
        elif self.lang == "js":
            compiler = JsCompiler(self.lang)
        elif self.lang == "rb":
            compiler = RubyCompiler(self.lang)
        return compiler

    def mv_files(self, output_path: str, files: List[str], repo_name: str):
        for f in files:
            splitted_file_path = f.split("/")
            file_name = splitted_file_path[-1]
            idx = splitted_file_path.index(repo_name) + 1
            file_path = "/".join([p for p in splitted_file_path[idx:-1]])
            if not os.path.exists(f"{output_path}{file_path}"):
                os.makedirs(f"{output_path}{file_path}")
            if os.path.exists(f"{output_path}{file_path}/{file_name}"):
                print(f"exists {file_name}")
                continue
            if os.path.exists(f):
                print(f"exists: {f}")
            print(f"move {f} > {output_path}{file_path}")
            shutil.move(f, f"{output_path}{file_path}")
