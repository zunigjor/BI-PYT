# Homework 01 - Game of life
# 
# Your task is to implement part of the cell automata called
# Game of life. The automata is a 2D simulation where each cell
# on the grid is either dead or alive.
# 
# State of each cell is updated in every iteration based state of neighbouring cells.
# Cell neighbours are cells that are horizontally, vertically, or diagonally adjacent.
#
# Rules for update are as follows:
# 
# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
#
# 
# Our implementation will use coordinate system will use grid coordinates starting from (0, 0) - upper left corner.
# The first coordinate is row and second is column.
# 
# Do not use wrap around (toroid) when reaching edge of the board.
# 
# For more details about Game of Life, see Wikipedia - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life


def createBoard(rows, cols):
    board = [[False] * cols for i in range(rows)]
    return board


def fillBoard(board, alive):
    for j in alive:
        x, y = j
        board[x][y] = True
    return None


def isAlive(board, x, y, rows, cols):
    if x < 0 or x >= rows:
        return False
    if y < 0 or y >= cols:
        return False
    return board[x][y]


def sumAliveNeighbors(board, r, c, rows, cols) -> int:
    sumN = 0
    sumN += isAlive(board, r - 1, c, rows, cols)  # up
    sumN += isAlive(board, r + 1, c, rows, cols)  # down
    sumN += isAlive(board, r, c - 1, rows, cols)  # left
    sumN += isAlive(board, r, c + 1, rows, cols)  # right
    sumN += isAlive(board, r - 1, c - 1, rows, cols)  # up left
    sumN += isAlive(board, r - 1, c + 1, rows, cols)  # up right
    sumN += isAlive(board, r + 1, c - 1, rows, cols)  # down left
    sumN += isAlive(board, r + 1, c + 1, rows, cols)  # down right
    return sumN


def makeGameStep(current_board, rows, cols):
    next_board = createBoard(rows, cols)
    for r in range(rows):
        for c in range(cols):
            sumN = sumAliveNeighbors(current_board, r, c, rows, cols)
            if current_board[r][c]:
                if sumN < 2 or sumN > 3:
                    next_board[r][c] = False
                if sumN == 2 or sumN == 3:
                    next_board[r][c] = True
            else:
                if sumN == 3:
                    next_board[r][c] = True
    current_board = next_board
    return current_board


def getAliveSet(board, rows, cols):
    result = set()
    for row in range(rows):
        for column in range(cols):
            if board[row][column]:
                t = (row, column)
                result.add(t)
    return result


def update(alive, size, iter_n):
    rows, cols = size
    current_board = createBoard(rows, cols)
    fillBoard(current_board, alive)
    i = 0
    while i < iter_n:
        current_board = makeGameStep(current_board, rows, cols)
        i += 1
    # Return the set of alive cells from the last current_board
    return getAliveSet(current_board, rows, cols)


def draw(alive, size):
    """
    alive - set of cell coordinates marked as alive, can be empty
    size - size of simulation grid as  tuple - ( 

    output - string showing the board state with alive cells marked with X
    """
    # Don't call print in this method, just return board string as output.
    # Example of 3x3 board with 1 alive cell at coordinates (0, 2):
    # +---+ 
    # |  X|
    # |   |
    # |   |
    # +---+
    rows, cols = size
    outputString = "+"
    for i in range(cols):
        outputString += "-"
    outputString += "+\n"
    for i in range(rows):
        outputString += "|"
        for j in range(cols):
            if (i, j) in alive:
                outputString += "X"
            else:
                outputString += " "
        outputString += "|\n"
    outputString += "+"
    for i in range(cols):
        outputString += "-"
    outputString += "+"
    return outputString
