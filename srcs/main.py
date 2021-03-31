import click

from game import Game
from parser import parser


@click.command()
@click.option(
    "--size",
    default=3,
    type=int,
    help="Input a puzzel size to generate a start puzzel, default value is 3",
)
@click.option(
    "--file",
    type=click.Path(exists=True, readable=True),
    help="Input a puzzel file path",
)
def main(file, size):
    """Program that solve N-puzzel game"""

    if file:
        puzzel_size, puzzel = parser(file)
        game = Game(puzzel_size, puzzel)
    elif size:
        game = Game(size)
    else:
        raise SystemExit("Need puzzel size or puzzel file")
    import ipdb

    ipdb.set_trace()


if __name__ == "__main__":
    main()
