import os
import git
from typing import List
from utils import extract_feature

class Crawler:

    def __init__(
        self,
        clone_dir: str = 'repositories',
        *,
        lang: str,
    ) -> None:
        self.lang = lang
        self.clone_dir = clone_dir


    def crawl(self, target_file_path: str):
        target_urls = self.get_target_urls(target_file_path)
        for url in target_urls:
            url = url.rstrip()
            user = url.split('/')[-2]
            repo_name = url.split('/')[-1]
            feature = extract_feature(target_file_path)
            if self.check_cache(user, repo_name):
                print(f'exists {user}/{repo_name}')
                continue
            self.clone(url, feature, user, repo_name)
            print(f'clone finished {user}/{repo_name}')
        return f'{self.clone_dir}/{self.lang}'

    @staticmethod
    def get_target_urls(target_file_path: str) -> List[str]:
        with open(target_file_path) as f:
            return f.readlines()

    def clone(self, url: str, feature: str, user: str, repo_name: str) -> None:
        to_path = f'{self.clone_dir}/{feature}/{self.lang}/{user}-{repo_name}'
        git.Repo.clone_from(
            url,
            to_path
        )

    def check_cache(self, user: str, repo_name: str):
        return os.path.exists(f'{self.clone_dir}/{self.lang}/{user}-{repo_name}')
