import re
import glob
import os
import token
import tokenize
from transformers import BertTokenizer

file_name = 'print-bytecode/various/py/alexander-akhmetov-python-telegram.git/telegram/client.py.pyc.txt'


class BaseNormalizer:
    def __init__(self) -> None:
        pass

    # def count_tokens(self, text: str):
    #     tokens = tokenize.generate_tokens(lambda L=iter(text.splitlines(True)): next(L))
    #     return sum(1 for _ in tokens if _[0] != token.INDENT and _[0] != token.DEDENT)


class PythonBytecodeNormalizer(BaseNormalizer):

    def normalize(self, file_path: str, tokenizer: BertTokenizer) -> list[str]:
        print(f"normalize {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            outputs = self.extract(content, tokenizer)
            return [output.strip() for output in outputs]

    def extract(self, text: str, tokenizer: BertTokenizer) -> list[str]:
        splitted_function_lines = text.split('Disassembly of ')
        function_lines = ['Disassembly of ' + l if l.startswith('<code object') else l for l in splitted_function_lines]
        # function_lines = [l.replace("maloss-sample/py/", "dataset/py/test").replace("", "") for l in function_lines]
        normalized_function_lines = []
        for function_line in function_lines:
           normalized_function_lines.extend(self.normalized_function_line(function_line, tokenizer))
        return normalized_function_lines
    
    def normalized_function_line(self, function_line: str, tokenizer: BertTokenizer):
        header = self._extract_header(function_line)
        if header:
            header = header.replace("maloss-sample/py/", "").replace("maloss-sample/python/", "").replace("maloss_sample/python/", "")
            header = header.replace("dataset/py/test/", "")
        lines = function_line.split('\n')
        normalized_lines = []
        pattern = re.compile(r"[a-zA-Z_]+")
        for line in lines:
            if not line or line == header:
                continue
            line = line.replace("maloss-sample/py/", "").replace("maloss-sample/python/", "").replace("maloss_sample/python/", "")
            line = line.replace("dataset/py/test/", "")
            splitted_lines = line.split("  ")
            splitted_lines = [l for l in splitted_lines if l]
            splitted_lines = [l.lstrip() for l in splitted_lines]
            splitted_lines = [l.replace(">> ", "") if l.startswith(">>") else l for l in splitted_lines]
            splitted_lines = [l for l in splitted_lines if l != ">>"]
            index = self.find_mnemonic_index(splitted_lines)
            mnemonic = pattern.findall(splitted_lines[index])[0]
            op = " ".join(splitted_lines[index + 1:]) if len(splitted_lines) >= index + 2 else ""
            normalized_lines.append(f"{mnemonic} {op}")
        # output = "\n".join(normalized_lines)
        output = "  ".join(normalized_lines)
        # print(output)
        if len(tokenizer.tokenize(f"{header} {output}")) > 512:
            return self.split_output_by_token_count(normalized_lines, tokenizer, header)
        else:
            return [f"{header} {output}"]
    
    @staticmethod
    def _extract_header(line: list[str]):
        splitted_lines = line.split(":\n")
        if splitted_lines[0].startswith("Disassembly of "):
            return splitted_lines[0] + ':'
        return ''

    def find_mnemonic_index(self, line: list[str]) -> int:
        mnemonic_index = 0
        if line[mnemonic_index].isdigit():
            mnemonic_index += 1
        if ">>" in line[mnemonic_index]:
            mnemonic_index += 1
        return mnemonic_index

    def split_output_by_token_count(self, normalized_lines: list[str], tokenizer, header) -> str:
        sentences = []
        sentence = ""
        for line in normalized_lines:
            sentence += (line + "  ")
            if ("RETURN_VALUE" in line or "STORE_NAME" in line) and len(tokenizer.tokenize(sentence)) > 300:
                sentence = f"{header} {sentence}" if header else sentence
                sentences.append(sentence)
                sentence = ""
        if sentence:
            sentence = f"{header} {sentence}" if header else sentence
            sentences.append(sentence)
        return sentences


class RubyBytecodeNormalizer(BaseNormalizer):

    def normalize():
        pass
    

class BytecodeNormalizer:

    def __init__(self, target_path: str, extension: str) -> None:
        self.target_path = target_path
        self.extension = extension
        self.result = {}
    
    def _guess_lang(self, file_path: str) -> str:
        if file_path.endswith("jsc.txt"):
            return "js"
        elif file_path.endswith("pyc.txt"):
            return "py"
        elif file_path.endswith("rbc.txt"):
            return "rb"
        return ""
    
    def normalize_all(self, output_path: str) -> None:
        file_paths = glob.glob(f"./{self.target_path}/**/*.{self.extension}", recursive=True)
        for file_path in file_paths:
            self.result[file_path] = self.normalize(file_path)
        self.output(output_path)

    def normalize(self, file_path: str) -> list[str]:
        normalizer = self.handle_normalizer(file_path)
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        return normalizer.normalize(file_path, tokenizer)

    def handle_normalizer(self, file_path: str) -> list[str]:
        lang = self._guess_lang(file_path)
        if lang == "py":
            return PythonBytecodeNormalizer()
        elif lang == "rb":
            return RubyBytecodeNormalizer()
        else:
            return None

    def output(self, output_path: str) -> None:
        if output_path.endswith("/"):
            output_path = output_path[:-1]
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        # self._output_one_file(output_path)
        self._output_each_files(output_path)

    def _output_one_file(self, output_path: str):
        output = f"{output_path}/output.txt"
        with open(output, "w", encoding="UTF-8", newline='\n') as f:
            f.writelines([row + "\n" for results_list in self.result.values() for row in results_list])
    
    def _output_each_files(self, output_path: str):
        for file_name, lines in self.result.items():
            file_name = file_name.replace(f"./{self.target_path}", "")
            file_name = file_name[1:] if file_name.startswith("/") else file_name
            dir_path = "/".join(file_name.split("/")[:-1])
            dir_path = f"{output_path}/{dir_path}"
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            file_name = file_name.replace(".py.pyc.txt", "")
            file_name = file_name.split("/")[-1]
            print(f"output: {dir_path}/{file_name}.txt")
            with open(f"{dir_path}/{file_name}.txt", "w", encoding="UTF-8", newline='\n') as f:
                f.writelines([row + "\n" for row in lines])
