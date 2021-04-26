import numpy as np

def directions(board, zero=None):
    if not zero:
        zero = np.where(board == 0)
    max_p = len(board) - 1
    if any(x < 0 or x > max_p for x in zero):
        raise RuntimeError("Zero is outside the game board")
    directions = ["left", "right", "up", "down"]
    if zero[1] == 0:
        directions.remove("left")
    if zero[1] == max_p:
        directions.remove("right")
    if zero[0] == 0:
        directions.remove("up")
    if zero[0] == max_p:
        directions.remove("down")
    return directions, zero

def moved_board(board, direction, zero=None):
    if not zero:
        zero = np.where(board == 0)
    new = board.copy()
    if direction == "left":
        des = (zero[0], zero[1] - 1)
    elif direction == "right":
        des = (zero[0], zero[1] + 1)
    elif direction == "up":
        des = (zero[0] - 1, zero[1])
    elif direction == "down":
        des = (zero[0] + 1, zero[1])
    new[des], new[zero] = new[zero], new[des]
    # print(
    #     f"zero({zero}) move {direction} \n Destination({des})\n new board:\n {new}"
    # )
    return new

def manhatten_dis(po, po_goal):
    return int(abs(po[0] - po_goal[0]) + abs(po[1] - po_goal[1]))

def h_cost(board, goal):
    """
    sum each distance between tile position and tile goal position
    except the Zero tile
    """

    total_dis = 0
    ite = np.nditer(board, flags=['multi_index'])
    for x in ite:
        if x == 0:
            continue
        po = ite.multi_index
        po_goal = np.where(goal == x)
        if po == po_goal:
            continue # This point is in the right position, distance = 0
        else:
            total_dis += manhatten_dis(po, po_goal)
    return total_dis


class Node:
    def __init__(self, board, fcost=None, parent=None):
        self.board = board
        self.fcost = fcost
        self.parent = parent
    
    def __hash__(self):
        return hash(self.board.tobytes())

    def __eq__(self, other):
        return np.array_equal(self.board, other.board)

def backtracking(node):
    lst = []
    while node.parent:
        lst.insert(0, node.parent)
        node = node.parent
    for x in lst:
        print(x.board)

def a_star(game):
    opend = dict()
    closed = dict()
    opencount = 0
    g = 0
    current = Node(game.start, fcost=h_cost(game.start, game.goal) + g)
    opend[current] = current
    opencount += 1

    def cmp_fcost(x):
        return x.fcost

    while opend:
        current = min(opend.values(), key=cmp_fcost)
        closed[current] = current
        opend.pop(current)
        
        if np.array_equal(current.board, game.goal):
            backtracking(current)
            print(f"complexity in time:{opencount}")
            return True
        drcs, zero = directions(current.board)
        g += 1
        for drc in drcs:
            new = moved_board(current.board, drc, zero=zero)
            child = Node(new)

            if child in closed:
                continue
            h = h_cost(child.board, game.goal)
            if child in opend:
                old = opend[child]
                if h + g < old.fcost:
                    old.fcost = g + h
                    old.parent = current
            else:
                child.fcost = h + g
                child.parent = current
                opend[child] = child
                opencount += 1



    print("NOT found !!!!!")
