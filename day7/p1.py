def main():
    matrix = []
    with open("input.txt", "r") as file:
        matrix = [list(line.strip()) for line in file]
        height = len(matrix)
        width = len(matrix[0])

        s_coor = matrix[0].index("S")

        current_beam_coors = [s_coor]
        split_count = 0

        for row_i in range(1, height):
            next_row_beam_coors = []

            for beam_col in current_beam_coors:
                if matrix[row_i][beam_col] == "^":
                    split_count += 1
                    next_row_beam_coors.append(beam_col - 1)
                    next_row_beam_coors.append(beam_col + 1)
                else:
                    next_row_beam_coors.append(beam_col)

            # we get the set here since sometimes 2 beams converge into one
            # and they only count as 1 split
            current_beam_coors = list(set(next_row_beam_coors))
            print(next_row_beam_coors)

        print(split_count)

main()
