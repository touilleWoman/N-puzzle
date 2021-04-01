import numpy as np


class Game:
    def __init__(self, puzzel_size, puzzel=None):
        """init game with start board"""

        self.p_size = puzzel_size
        if puzzel:
            self.start = np.asarray(puzzel)
        else:
            self.random_start()
        # self.board = self.start.copy()
        self.check_board()
        # self.zero = self.position_of_zero()
        self.goal = self.generate_goal()

    def random_start(self):
        self.start = np.random.choice(
            [x for x in range(0, self.p_size * self.p_size)],
            replace=False,
            size=(self.p_size, self.p_size),
        )

    # def position_of_zero(self):
    #     return np.where(self.board == 0)

    # def directions(self, zero=None):
    #     if not zero:
    #         zero = self.position_of_zero()
    #     if any(x < 0 or x > self.p_size for x in zero):
    #         raise RuntimeError("Zero is outside the game board")
    #     directions = ["left", "right", "up", "down"]
    #     if zero[1] == 0:
    #         directions.remove("left")
    #     if zero[1] == self.p_size - 1:
    #         directions.remove("right")
    #     if zero[0] == 0:
    #         directions.remove("up")
    #     if zero[0] == self.p_size - 1:
    #         directions.remove("down")
    #     return directions

    def check_board(self):
        if self.start.shape != (self.p_size, self.p_size):
            raise RuntimeError("Wrong shape of board:", self.start.shape)
        if not np.array_equal(np.unique(self.start), np.arange(self.start.size)):
            raise RuntimeError("Wrong element value of board:", self.start)
        print(f"Game board checked, all good ^^\n{self.start}")

    # def move_zero(self, direction, zero=None):
    #     if not zero:
    #         zero = self.position_of_zero()

    #     if direction not in self.directions(): # delete later
    #         raise RuntimeError("Error: Got out of the game board")


    #     if direction == "left":
    #         des = (zero[0], zero[1] - 1)
    #     elif direction == "right":
    #         des = (zero[0], zero[1] + 1)
    #     elif direction == "up":
    #         des = (zero[0] - 1, zero[1])
    #     elif direction == "down":
    #         des = (zero[0] + 1, zero[1])
    #     self.board[des], self.board[zero] = self.board[zero], self.board[des]
    #     print(
    #         f"zero({zero}) move {direction} \n Destination({des})\n board:\n {self.board}"
    #     )
    #     zero = des

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
        # print("goal:\n", board)
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
