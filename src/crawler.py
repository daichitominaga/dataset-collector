import os
import git
from typing import List
from src.utils import extract_feature

class Crawler:

    def __init__(
        self,
        clone_dir: str = 'repositories',
        *,
        lang: str,
    ) -> None:
        self.lang = lang
        self.clone_dir = clone_dir


    def crawl(self, target_file_path: str, output: str = ''):
        target_urls = self.get_target_urls(target_file_path)
        for url in target_urls:
            url = url.rstrip()
            user = url.split('/')[-2]
            repo_name = url.split('/')[-1]
            if not output:
                feature = extract_feature(target_file_path)
                output = f"{self.clone_dir}/{feature}/{self.lang}/"
            if self.check_cache(output, user, repo_name):
                print(f'exists {user}/{repo_name}')
                continue
            self.clone(url, user, repo_name, output)
            print(f'clone finished {user}/{repo_name}')
        output = output if output else f'{self.clone_dir}/{self.lang}'
        return output

    @staticmethod
    def get_target_urls(target_file_path: str) -> List[str]:
        with open(target_file_path) as f:
            return f.readlines()

    def clone(self, url: str, user: str, repo_name: str, output: str) -> None:
        to_path = f'{output}/{user}-{repo_name}'
        git.Repo.clone_from(
            url,
            to_path
        )

    def check_cache(self, output: str, user: str, repo_name: str):
        return os.path.exists(f'{output}/{user}-{repo_name}')
