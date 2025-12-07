# I tried to solve it by computing the permutation at the end but it didnt work
# Thought DP might work here.
# Instead of tracking WHAT the paths are, track HOW MANY paths there are
# And we can do that by recording the amounts at each step.
# I need to get better at DP ._.

def main():
    matrix = []
    with open("input.txt", "r") as file:
        matrix = [list(line.strip()) for line in file]
        height = len(matrix)
        width = len(matrix[0])

        s_coor = matrix[0].index("S")

        # current[col] = number of different paths reaching this column for current ROW step
        current = {s_coor: 1}

        for row_i in range(1, height):
            print(f"Current for row {row_i}:", current)
            next_paths = {}

            for col, count in current.items():
                if matrix[row_i][col] == "^":
                    left_col = col - 1
                    right_col = col + 1

                    # Only add if within bounds
                    if left_col >= 0:
                        next_paths[left_col] = next_paths.get(left_col, 0) + count
                    if right_col < width:
                        next_paths[right_col] = next_paths.get(right_col, 0) + count
                else:
                    next_paths[col] = next_paths.get(col, 0) + count

            current = next_paths

        total = sum(current.values())
        print(f"Number of timelines: {total}")

main()
