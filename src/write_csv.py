import os
import csv
import random
import glob
import json


class WriteCSVDateSet:

    def write_all(self, directory: str, label: int):
        embed_tables = self._load_embed_tables()
        embedded_file_resolver = {
            t['original_source'].split("/")[-1]: t['embedded_source'] for t in embed_tables
        }
        text_files = self.get_text_files(directory)
        rows = []
        for text_file in text_files:
            file_path = os.path.join(directory, text_file)
            content_list = self.read_and_split_file(file_path)
            # embed_file_name = embedded_file_resolver[text_file.replace(".txt", ".py")]
            # file_name = "_".join(embed_file_name.split('/')[-2:])
            rows.append((text_file, label, content_list))
        self.write_to_csv(rows)
    
    def write_random_files(self, directory: str, num_files: int, label: int):
        embed_tables = self._load_embed_tables()
        original_files = [t["original_source"] for t in embed_tables]
        text_files = self.get_random_files(directory, num_files, original_files)
        rows = []
        for text_file in text_files:
            content_list = self.read_and_split_file(text_file)
            file_name = text_file.split('/')[-1]
            rows.append((file_name, label, content_list))
        self.write_to_csv(rows)
    
    @staticmethod
    def _load_embed_tables():
        with open('embed_malicious_codes/py/embed_tables.json') as f:
            return json.load(f)

    def get_random_files(self, directory, num_files, original_files):
        files = glob.glob(f"./{directory}/**/*.txt", recursive=True)
        # for i, p in enumerate(original_files[0].split('/')):
        #     if p == 'py':
        #         original_extension_index = i
        #         break
        # for i, p in enumerate(original_files[0].split('/')):
        #     if p == 'py':
        #         target_extension_index = i
        #         break
        # original_file_paths = [self.convert_file_path(original_extension_index, file) for file in original_files]
        # excluded_files = []
        # print(original_file_paths)
        # for f in files:
        #     if self.convert_file_path(target_extension_index, f).replace(".txt", ".py") in original_file_paths:
        #         continue
        #     excluded_files.append(f)
        random_files = random.sample(files, num_files)
        return random_files

    @staticmethod
    def convert_file_path(index, file_path):
        return "/".join(file_path.split('/')[(index+1):])

    @staticmethod
    def get_text_files(directory):
        return [f for f in os.listdir(directory) if f.endswith('.txt')]

    @staticmethod
    def read_and_split_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content.splitlines()

    @staticmethod
    def write_to_csv(data):
        with open(f'dataset_source_code_learn.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(("file_name", "label", "code"))
            for row in data:
                csvwriter.writerow(row)
