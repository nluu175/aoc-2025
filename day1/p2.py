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
    cycles_traveled = 0

    if moves < 0:
        # aka. Check if we wrapped around (crossed 0 at least once)
        # new_point > starting_point means we cross 0
        # starting_point != 0 is used for eliminating false positive
        if new_point > starting_point and starting_point != 0:
            cycles_traveled += 1
    else:
        # new_point < starting_point means we cross 0
        # new_point != 0 since it's already handled in main loop
        if new_point < starting_point and new_point != 0:
            cycles_traveled += 1

    cycles_traveled += abs(moves) // 100

    return new_point, cycles_traveled


def main():
    current_point = 50
    zero_counter = 0

    with open("input.txt", "r") as file:
        for line in file:
            moves = decode_rotation(line.strip())
            prev_point = current_point
            current_point, cycles_traveled = execute_rotation(current_point, moves)

            print(
                f"Prev: {prev_point},     Move: {moves},      Current: {current_point},      Cycles Traveled: {cycles_traveled}"
            )

            if current_point == 0:
                zero_counter += 1
            zero_counter += cycles_traveled

    print(zero_counter)


main()
