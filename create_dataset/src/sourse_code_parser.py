import ast
from black import format_file_contents, FileMode
from transformers import BertTokenizer


class SourceCodeParser:

    def parse(self, file_path: str):
        print(f"parse start: {file_path}")
        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        all_elements = self.get_imports_and_functions(file_path)
        print(f"parse finish: {file_path}")
        return self.to_list_str(all_elements, tokenizer)
    
    def to_list_str(self, all_elements: list, tokenizer: BertTokenizer) -> list[str]:
        str_array = []
        current_str = ""

        for element_type, class_name, class_line, code, _ in all_elements:
            element_str = ""

            if element_type == 'Import':
                element_str = f'{code}'
            elif element_type == 'ClassMethod':
                element_str = f'{class_line}\n{code}'
            elif element_type == 'Function':
                element_str = f'{code}'
            elif element_type == 'Other':
                element_str = f'{code}'

            element_str += '\n'

            if len(tokenizer.tokenize(element_str)) > 350:
                str_array.append(current_str)
                current_str = ""

            current_str += element_str

        if current_str:
            str_array.append(current_str)
        return str_array

    def get_imports_and_functions(self, file_path: str) -> list:
        self.apply_black(file_path)
        try:
            with open(file_path) as f:
                source = f.read()
        except:
            source = None
        if not source:
            return []

        tree = ast.parse(source, file_path)
        all_elements = []

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                all_elements.append(('Import', None, None, source.split('\n')[node.lineno-1], node.lineno))

            elif isinstance(node, ast.ClassDef):
                class_name = node.name
                class_line = source.split('\n')[node.lineno-1]
                for method in node.body:
                    if isinstance(method, ast.FunctionDef):
                        method_code = self.get_function_code(method, source)
                        all_elements.append(('ClassMethod', class_name, class_line, method_code, method.lineno))

            elif isinstance(node, ast.FunctionDef):
                function_code = self.get_function_code(node, source)
                all_elements.append(('Function', None, None, function_code, node.lineno))

            else:
                other_code = '\n'.join(source.split('\n')[node.lineno-1:node.end_lineno])
                all_elements.append(('Other', None, None, other_code, node.lineno))

        all_elements.sort(key=lambda x: x[4])

        return all_elements

    def apply_black(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8-sig") as f:
                source = f.read()
        except:
            source = None
        if not source:
            return

        mode = FileMode()

        try:
            formatted_source = format_file_contents(source, mode=mode, fast=True)
        except Exception as e:
            print(f"Black formatting failed: {e}")
            return

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(formatted_source)
    
    def get_function_code(self, method, source):
        start_line = method.lineno - 1
        method_code = source.split('\n')[start_line:method.end_lineno]
        for decorator in method.decorator_list:
            method_code.insert(0, source.split('\n')[decorator.lineno-1])
        return '\n'.join(method_code)
