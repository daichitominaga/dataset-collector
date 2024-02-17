## 機能
- GitHubリポジトリをクローリングします。提供されたURLリストに基づいています。
- クロールしたリポジトリからソースコードをコンパイルします。
- コンパイルされたファイルのバイトコードを出力します。
- Pythonファイルに対してBanditセキュリティ分析を実行します。
- 分析のために文字列とバイトコードを正規化します。
- 特定のパターンを抽出するためにソースコードを解析します。
- 与えられたURLからウェブコンテンツをスクレイピングします。
- 分析用のカスタマイズ可能なラベルでCSVデータセットを作成します。

## インストール
このツールキットはPython 3.7以降が必要です。リポジトリをクローンして依存関係をインストールします

```bash
git clone <url>
cd research-malicious-code/create_dataset
poetry install
```

## 使用方法
各機能はコマンドとして提供されます。langは現在pythonしかサポートされていません

1. クローリング
.txtファイルにリストされたGitHubリポジトリをクロールします。

```bash
poetry run python main.py crawl --target path/to/urls.txt --lang <lang> --output <output_dit>
```

2. コンパイル
GitHubリポジトリのソースコードをコンパイルします。

```bash
poetry run python main.py compile --target path/to/repository --lang <lang> --all --output <output_dit>
```

3. バイトコードの出力
コンパイルされたファイルのバイトコードを生成して出力します。

```bash
poetry run python main.py print_bytecode --target path/to/repository --lang <lang> --all --output <output_dit>
```

4. Banditの実行
Pythonファイルに対してBanditセキュリティ分析を実行します。

```bash
poetry run python main.py run_bandit --target path/to/repository --output <output_dit>
```

5. 文字列の正規化
分析のためにコンパイルされたファイル内の文字列を正規化します。

```bash
poetry run python main.py normalize_string --target path/to/compiled/files --output <output_dit>
```

6. バイトコードの正規化
分析のためにバイトコードを正規化します。

```bash
poetry run python main.py normalize_bytecode --target path/to/compiled/files --extension .pyc --lang <lang> --output <output_dit>
```

7. ソースコードの解析
特定のパターンを抽出するためにソースコードを解析します。

```bash
python main.py parse_source_code --target path/to/source/code --all --label <label>
```

8. スクレイピング
指定されたURLリストからウェブコンテンツをスクレイピングします。

```bash
python main.py scraping --target path/to/urls.txt --output <output_dit>
```

9. CSVの作成
分析のためにCSVデータセットを作成します。

```bash
python main.py write_csv --target path/to/compiled/files --label <label>
```
