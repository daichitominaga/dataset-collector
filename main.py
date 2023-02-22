import click
import os
from src.crawler import Crawler
from src.compiler import Compiler
from src.normalizer import BytecodeNormalizer
from src.scraper import WebScraper


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
def crawl(target: str, lang: str):
    crawler = Crawler(lang=lang)
    crawler.crawl(target)


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
def compile(target: str, lang: str, all: bool):
    if all:
        target = target if target.endswith('/') else target + '/'
        files = [target + f for f in os.listdir(target)]
    else:
        files = [target[:-1]] if target.endswith('/') else [target]
    for f in files:
        compiler = Compiler(lang=lang)
        compiler.compile(f)


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
def normalize(target: str, output: str):
    normalizer = BytecodeNormalizer(target=target)
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
    '--output',
    type=str,
    required=True,
    help='Path of the output'
)
def scraping(target: str, output: str):
    output = output[:-1] if output.endswith("/") else output
    scraper = WebScraper(output_dir=output, target_file_path=target)
    for url in scraper.targets:
        if os.path.exists(scraper.output_path(url)):
            continue
        scraper.scraping(url)
        scraper.output(url)
    scraper.output_result_file()


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
    