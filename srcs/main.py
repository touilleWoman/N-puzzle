import click
import numpy as np

from parser import parser


class Point:
    """
        Position on the game board
        x represents vertical line
        y represents horizental line
        edge represents outer line of board, point can't go outside of edge
        The uper left corner point is (0, 0)
    """

    def __init__(self, x, y, puzzel_size):
        self.x = x
        self.y = y
        self.edge = puzzel_size

    def go_right(self):
        if self.y + 1 >= self.edge:
            return False
        self.y += 1
        return True

    def go_down(self):
        if self.x + 1 >= self.edge:
            return False
        self.x += 1
        return True

    def go_left(self):
        if self.y - 1 < 0:
            return False
        self.y -= 1
        return True

    def go_up(self):
        if self.x - 1 < 0:
            return False
        self.x -= 1
        return True


class Game:
    def __init__(self, puzzel_size, puzzel):
        self.puzzel_size = puzzel_size
        self.starting_board = np.asarray(puzzel)
        self.board = self.starting_board.copy()
        self.check_board()
        self.generate_object_board()

    def check_board(self):
        if self.board.shape != (self.puzzel_size, self.puzzel_size):
            raise RuntimeError('Wrong shape of board:', self.board.shape)
        if not np.array_equal(np.unique(self.board), np.arange(self.board.size)):
            raise RuntimeError('Wrong element value of board:', self.board)
        print("Game board checked, all good ^^")
    
    def generate_object_board(self):
        p = Point(0, -1, self.puzzel_size)
        board = np.zeros((self.puzzel_size, self.puzzel_size), dtype=int)
        count = self.board.size
        value = 1
        while value < self.board.size:
            while p.go_right() and value < self.board.size:
                if board[p.x, p.y] == 0:
                    board[p.x, p.y] = value
                    value += 1
                else:
                    p.go_left()
                    break
                print(board)
            while p.go_down() and value < self.board.size:
                if board[p.x, p.y] == 0:
                    board[p.x, p.y] = value
                    value += 1
                else :
                    p.go_up()
                    break
                print(board)

            while p.go_left() and value < self.board.size:
                if board[p.x, p.y] == 0:
                    board[p.x, p.y] = value
                    value += 1
                else:
                    p.go_right()
                    break
                print(board)
            while p.go_up() and value < self.board.size:
                if board[p.x, p.y] == 0:
                    board[p.x, p.y] = value
                    value += 1
                else:
                    p.go_down()
                    break
                print(board)

        print('done----')  

        




@click.command()
@click.argument("file_path", type=click.Path(exists=True, readable=True))
def main(file_path):
    """Program that solve N-puzzel game"""

    if file_path:
        puzzel_size, puzzel = parser(file_path)
        game = Game(puzzel_size, puzzel)

if __name__ == "__main__":
    main()
