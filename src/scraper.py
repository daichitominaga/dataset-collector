import os
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from typing import List


class WebScraper:

    def __init__(self, output_dir: str, target_file_path: str = []) -> None:
        self.output_dir = output_dir
        self.soup = None
        self.targets = [url.rstrip() for url in self.get_target_urls(target_file_path)]
        self.result = []

    def scraping(self, url: str) -> None:
        res = requests.get(url)
        self.soup = BeautifulSoup(res.content, 'html.parser')

    def output(self, url: str) -> None:
        if not self.soup:
            raise Exception
        output_path = self.output_path(url)
        output_dir = "/".join(output_path.split("/")[:-1])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        write_lines = []
        with open(output_path, "w", encoding="UTF-8", newline='\n') as f:
            for line in self.soup.text.split('\n'):
                if not line:
                    continue
                f.writelines(line)
                write_lines.append(line)
        self.result.extend(write_lines)
        
    def output_result_file(self):
        with open(self.output_dir, "w", encoding="UTF-8", newline='\n') as f:
            for line in self.result:
                f.writelines(line)
    
    def output_path(self, url: str):
        parsed_url = urlparse(url)
        return f"{self.output_dir}/{parsed_url.netloc}/{parsed_url.path.split('/')[-1]}/output.txt"

    @staticmethod
    def get_target_urls(target_file_path: str) -> List[str]:
        with open(target_file_path) as f:
            return f.readlines()
    

    def collect_dataset_target(target_url: str, target_pages: int, page_number_query_key_name: str, current_page_num: int = 0):
        for i in range(target_pages):
            page_num = i + current_page_num
            target = f"{target_url}&{page_number_query_key_name}={page_num}"
            res = requests.get(target)
            print(f"collect page: {target}")
            soup = self.scraping(target)
            for url_click_area in soup.find_all('a', class_='v-align-middle'):
                payload = json.loads(url_click_area.attrs["data-hydro-click"]).get("payload", {})
                result = payload.get("result", {})
                url = result.get("url", "")
                if not url:
                    continue
                print(f"{url}.git")
    
