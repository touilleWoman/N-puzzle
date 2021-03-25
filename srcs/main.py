import click

from parser import parser


@click.command()
@click.argument("file_path", type=click.Path(exists=True, readable=True))
def main(file_path):
    """Program that solve N-puzzel game"""

    if file_path:
        matrix = parser(file_path)


if __name__ == "__main__":
    main()
