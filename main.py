import click
import os
from src.crawler import Crawler
from src.compiler import Compiler
from src.string_normalizer import StringNormalizer
from src.scraper import WebScraper
from src.bytecode_normalizer import BytecodeNormalizer
from src.write_csv import WriteCSVDateSet


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    '--target',
    type=str,
    required=True,
    help='Path to a .txt file containing the github url to be crawled'
)
@click.option(
    '--lang',
    type=str,
    required=True,
    help='Language in which the source code of the repository is written'
)
@click.option(
    '--output',
    type=str,
    required=False,
    help='output dir'
)
def crawl(target: str, lang: str, output: str = ""):
    crawler = Crawler(lang=lang)
    crawler.crawl(target, output)


@cli.command()
@click.option(
    '--target',
    type=str,
    required=True,
    help='Path of the github repository to compile'
)
@click.option(
    '--lang',
    type=str,
    required=True,
    help='Language in which the source code of the repository is written'
)
@click.option(
    '--all',
    is_flag=True,
    required=False,
    help='Language in which the source code of the repository is written'
)
@click.option(
    '--output',
    type=str,
    required=False,
    help='output dir'
)
def compile(target: str, lang: str, all: bool, output: str):
    if all:
        target = target if target.endswith('/') else target + '/'
        files = [target + f for f in os.listdir(target)]
    else:
        files = [target[:-1]] if target.endswith('/') else [target]
    for f in files:
        compiler = Compiler(lang=lang)
        compiler.compile(f, output)


@cli.command()
@click.option(
    '--target',
    type=str,
    required=True,
    help='Path of the github repository to print-bytecode'
)
@click.option(
    '--lang',
    type=str,
    required=True,
    help='Language in which the source code of the repository is written'
)
@click.option(
    '--all',
    is_flag=True,
    required=False,
    help='Language in which the source code of the repository is written'
)
@click.option(
    '--output',
    type=str,
    required=False,
    help='output dir'
)
def print_bytecode(target: str, lang: str, all: bool, output: str):
    if all:
        target = target if target.endswith('/') else target + '/'
        files = [target + f for f in os.listdir(target)]
    else:
        files = [target[:-1]] if target.endswith('/') else [target]
    for f in files:
        compiler = Compiler(lang=lang)
        compiler.print_bytecode(f, output)


@cli.command()
@click.option(
    '--target',
    type=str,
    required=True,
    help='Path of the compiled files dir'
)
@click.option(
    '--output',
    type=str,
    required=True,
    help='Path of the output'
)
def normalize_string(target: str, output: str):
    normalizer = StringNormalizer(target=target)
    normalizer.normalize_files()
    normalizer.output(output)


@cli.command()
@click.option(
    '--target',
    type=str,
    required=True,
    help='Path of the compiled files dir'
)
@click.option(
    '--extension',
    type=str,
    required=True,
    help='file extension'
)
@click.option(
    '--output',
    type=str,
    required=True,
    help='Path of the output'
)
def normalize_bytecode(target: str, extension: str, output: str):
    normalizer = BytecodeNormalizer(target_path=target, extension=extension)
    normalizer.normalize_all(output)


@cli.command()
@click.option(
    '--target',
    type=str,
    required=True,
    help='Path of the compiled files dir'
)
@click.option(
    '--output',
    type=str,
    required=True,
    help='Path of the output'
)
def scraping(target: str, output: str):
    output = output[:-1] if output.endswith("/") else output
    scraper = WebScraper(output_path=output, target_file_path=target)
    for url in scraper.targets:
        if os.path.exists(scraper.output_path(url)):
            continue
        scraper.scraping(url)
        scraper.output(url)
    scraper.output_result_file()


@cli.command()
@click.option(
    '--target',
    type=str,
    required=True,
    help='Path of the compiled files dir'
)
@click.option(
    '--label',
    type=int,
    required=True,
    help='code label (0: benign, 1: malicious)'
)
@click.option(
    '--file_num',
    type=int,
    required=False,
    default=0,
    help='collect random file num'
)
def write_csv(target: str, label: int, file_num: int):
    write_csv = WriteCSVDateSet()
    if file_num:
        write_csv.write_random_files(target, file_num, label)
    else:
        write_csv.write_all(target, label)


@cli.command()
@click.option(
    '--input',
    type=str,
    required=True,
    help='Path to a .txt file containing the github url to be crawled'
)
@click.option(
    '--lang',
    type=str,
    required=True,
    help='Language in which the source code of the repository is written'
)
def make_datasets(target: str, lang: str):
    crawler = Crawler(lang)
    crawled_repositories_path = crawler.crawl(target)

    compiler = Compiler(lang)
    compiler.compile(crawled_repositories_path)


if __name__ == '__main__':
    cli()
    