import copy

def is_able_to_access(board, i, j) -> bool:
    if board[i][j] != "@":
        return False

    rows = len(board)
    cols = len(board[0])

    # Define the 8 directions (neighbors)
    directions = [
        (-1, -1),  # top-left
        (-1, 0),  # top
        (-1, 1),  # top-right
        (0, -1),  # left
        (0, 1),  # right
        (1, -1),  # bot-left
        (1, 0),  # bot
        (1, 1),  # bot-right
    ]

    count = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        # Check if neighbor is in bounds
        if 0 <= ni < rows and 0 <= nj < cols:
            if board[ni][nj] == "@":
                count += 1

    return count < 4


def remove_accessible_rolls(board):
    copied_board = copy.deepcopy(board)
    counter = 0
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if is_able_to_access(board, i, j):
                counter += 1
                copied_board[i][j] = "."

    return counter, copied_board


def main():
    board = []
    counter = 0

    with open("input.txt", "r") as file:
        for line in file:
            board.append(list(line.strip()))

    counter_for_this_round = float('inf')

    # repeat until we cannot remove anymore paper
    while (counter_for_this_round > 0):
        counter_for_this_round, board = remove_accessible_rolls(board)
        counter += counter_for_this_round

    print(counter)


main()
