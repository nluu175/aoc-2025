# Some observations
# - Index of digit now matters since we cant treat the whole number as a column
# - White Space, White Space, 4 is treated as number 4 -> thus max width of all rows should be used as a width so that we dont miss any digits
# - Operator col index is the end boundary of the whole operation. This is the most reliable way to mark the end of the operation
# - I missed the operator index and was trying to split the operations based on the higher rows (number)
# - Taking Transpose of the matrix might be doable for this problem too. Will try later.
# - It doesn't really matter if we do it RIGHT TO LEFT or LEFT TO RIGHT (this part is confusing) since we treat each digit as its own entry and we only do (+) and (*) within each eperation group

def main():
    with open("input.txt", "r") as file:
        lines = [line.rstrip('\n') for line in file.readlines()]

    grid = [list(line) for line in lines]

    for i in range(len(grid)):
        print(f"Len row#{i}:", len(grid[i]))

    # set width to the max width so that we don't miss the white space
    # then pad all lines to the same width
    width = max(len(line) for line in grid)

    for i in range(len(grid)):
        while len(grid[i]) < width:
            grid[i].append(' ')

    height = len(grid)
    operator_line = height - 1

    total = 0
    operator_index = 0

    while operator_index < width:
        op_width = width - operator_index
        for i in range(operator_index + 1, width):
            if grid[operator_line][i] != ' ':
                op_width = i - operator_index - 1
                break

        current_row_operator = grid[operator_line][operator_index]

        accumulator = 1 if current_row_operator == '*' else 0

        # process columns LEFT-TO-RIGHT within this operation
        # for col in range(operator_index + op_width - 1, operator_index - 1, -1):
        for col in range(operator_index, operator_index + op_width):
            # build the number from TOP-TO-BOTTOM in this column
            num = 0
            for row in range(height - 1):
                if grid[row][col] != ' ':
                    digit = int(grid[row][col])
                    num = num * 10 + digit

            # assume that only has * or +
            if current_row_operator == '*':
                accumulator *= num
            else:
                accumulator += num

        total += accumulator

        operator_index += op_width + 1

    print(f"Grand Total: {total}")

main()
