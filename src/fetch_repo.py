import requests
import sys


def fetch_all_repos(language, per_page=100):
    page = 1
    all_repos = []

    while True:
        url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc&per_page={per_page}&page={page}"
        headers = {'Accept': 'application/vnd.github+json'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            repos = response.json()['items']
            if not repos:
                break

            for repo in repos:
                all_repos.append(repo['html_url'])

            print(f"ページ {page} を取得しました。")

            # GitHub APIのレート制限に達した場合、次のページは取得できません。
            if 'X-RateLimit-Remaining' in response.headers and int(response.headers['X-RateLimit-Remaining']) == 0:
                print("API レート制限に達しました。")
                break

            page += 1

        else:
            print(f"Error: {response.status_code}")
            break

    return all_repos


if __name__ == '__main__':
    # get args from command line
    args = sys.argv
    if len(args) == 3:
        language = args[1]
        per_page = args[2]
    else:
        print("引数が不正です。")
        print("例：python fetch_repo.py python 1")
        sys.exit()

    all_repos = fetch_all_repos(language, per_page=per_page)

    print(f"{language} のリポジトリのURL一覧：")
    for repo_url in all_repos:
        print(repo_url)
