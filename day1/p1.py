def decode_rotation(rotation):
    direction = rotation[:1]
    steps = int(rotation[1:])

    # assume that every rotation only starts with L or R
    if direction.upper() == "L":
        return (-1) * steps
    else:
        return steps


def execute_rotation(starting_point, moves):
    new_point = (starting_point + moves) % 100
    return new_point


def main():
    starting_point = 50
    zero_counter = 0

    with open("input.txt", "r") as file:
        for line in file:
            moves = decode_rotation(line.strip())
            starting_point = execute_rotation(starting_point, moves)

            if starting_point == 0:
                zero_counter += 1

    print(zero_counter)


main()
