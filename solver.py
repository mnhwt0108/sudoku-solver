# solver.py

def solve(bo):              # Use to find empty cell and solve for it
    find = find_empty(bo)
    if not find:            # If the board is full, stop (base case)
        return True
    else:                   # Else, return the value of position
        row, col = find

    for i in range(1, 10):  # Check and replace possible answer
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):  # Recursive call
                return True
            bo[row][col] = 0

    return False


def valid(bo, numb, pos):  # Check for validity of the cell
    # Check for row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == numb and pos[1] != i:
            return False

    # Check for column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == numb and pos[0] != i:
            return False

    # Check for box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):  # Note: 2D array so (i,j), different axis
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == numb and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - -")

        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):  # Find empty cells in the board
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i, j)
    return
