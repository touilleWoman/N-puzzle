import numpy as np


class Game:
    def __init__(self, puzzel_size, puzzel=None):
        """init game with start board, postition of zero """

        self.p_size = puzzel_size
        if puzzel:
            self.start_board = np.asarray(puzzel)
        else:
            self.random_start_board()
        self.board = self.start_board.copy()
        self.check_board()
        self.zero = self.position_of_zero()
        self.goal = self.generate_goal()

    def random_start_board(self):
        self.start_board = np.random.choice(
            [x for x in range(0, self.p_size * self.p_size)],
            replace=False,
            size=(self.p_size, self.p_size),
        )

    def position_of_zero(self):
        return np.where(self.board == 0)

    def directions(self):
        if any(x < 0 or x > self.p_size for x in self.zero):
            raise RuntimeError("Zero is outside the game board")
        directions = ["left", "right", "up", "down"]
        if self.zero[1] == 0:
            directions.remove("left")
        if self.zero[1] == self.p_size - 1:
            directions.remove("right")
        if self.zero[0] == 0:
            directions.remove("up")
        if self.zero[0] == self.p_size - 1:
            directions.remove("down")
        return directions

    def check_board(self):
        if self.board.shape != (self.p_size, self.p_size):
            raise RuntimeError("Wrong shape of board:", self.board.shape)
        if not np.array_equal(np.unique(self.board), np.arange(self.board.size)):
            raise RuntimeError("Wrong element value of board:", self.board)
        print("Game board checked, all good ^^")

    def move(self, direction):
        if direction not in self.directions():
            raise RuntimeError("Error: Got out of the game board")
        if direction == "left":
            des = (self.zero[0], self.zero[1] - 1)
        elif direction == "right":
            des = (self.zero[0], self.zero[1] + 1)
        elif direction == "up":
            des = (self.zero[0] - 1, self.zero[1])
        elif direction == "down":
            des = (self.zero[0] + 1, self.zero[1])
        self.board[des], self.board[self.zero] = self.board[self.zero], self.board[des]
        print(
            f"zero({self.zero}) move {direction} \n Destination({des})\n board:\n {self.board}"
        )
        self.zero = des

    def generate_goal(self):
        p = Point(0, -1, self.p_size)
        board = np.zeros((self.p_size, self.p_size), dtype=int)
        board_size = self.p_size * self.p_size
        value = 1

        while value < board_size:
            while p.go_right() and value < board_size:
                if board[p.x, p.y] == 0:
                    board[p.x, p.y] = value
                    value += 1
                else:
                    p.go_left()
                    break
            while p.go_down() and value < board_size:
                if board[p.x, p.y] == 0:
                    board[p.x, p.y] = value
                    value += 1
                else:
                    p.go_up()
                    break
            while p.go_left() and value < board_size:
                if board[p.x, p.y] == 0:
                    board[p.x, p.y] = value
                    value += 1
                else:
                    p.go_right()
                    break
            while p.go_up() and value < board_size:
                if board[p.x, p.y] == 0:
                    board[p.x, p.y] = value
                    value += 1
                else:
                    p.go_down()
                    break
        print("goal:\n", board)
        return board


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
