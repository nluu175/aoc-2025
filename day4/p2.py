# Some notes
# - The easiest solution is loop through the whole board and check adjacent cells
# - Part 2 requires redoing the whole process again and again until we cant remove anymore (aka. removed_counter = 0)
# - I tried deepcopy the board under every call to remove_accessible_rolls. This is expensive. Later replaced this
# with a tracker

def is_able_to_access(board, i, j) -> bool:
    if board[i][j] != "@":
        return False

    rows = len(board)
    cols = len(board[0])

    # Define the 8 directions (neighbors)
    directions = [
        (-1, -1),   # top-left
        (-1, 0),    # top
        (-1, 1),    # top-right
        (0, -1),    # left
        (0, 1),     # right
        (1, -1),    # bot-left
        (1, 0),     # bot
        (1, 1),     # bot-right
    ]

    count = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            if board[ni][nj] == "@":
                count += 1
                if count >= 4:  # early access to reduce the number of checks
                    return False

    return count < 4


def remove_accessible_rolls(board):
    rows = len(board)
    cols = len(board[0])

    # identify which rolls to remove
    to_remove = []
    for i in range(rows):
        for j in range(cols):
            if is_able_to_access(board, i, j):
                to_remove.append((i, j))

    # remove them
    for i, j in to_remove:
        board[i][j] = "."

    return len(to_remove)


def main():
    board = []
    total_counter = 0

    with open("input.txt", "r") as file:
        for line in file:
            board.append(list(line.strip()))

    rounds_counter = 0
    while True:
        rounds_counter += 1
        removed_counter = remove_accessible_rolls(board)
        if removed_counter == 0:
            break
        total_counter += removed_counter

    print(total_counter, rounds_counter)


main()
