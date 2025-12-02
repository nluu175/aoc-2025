# Some observations
# - Invalid ids are only ids with even number of digits
# - They follow this pattern
# - 2 digits - divided by 11
# - 4 digits - divivded by 101
# - 6 digits - divided by 1001


def parse_ranges(range_string):
    ranges = []
    for range_part in range_string.split(","):
        start, end = range_part.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(num):
    num_digits = len(str(num))

    if num_digits % 2 != 0:
        return False

    half_digits = num_digits // 2
    divisor = 10**half_digits + 1

    # Check if divisible by the divisor
    if num % divisor != 0:
        return False

    # Also check that the quotient doesn't have leading zeros
    # (quotient should have exactly half_digits digits)
    quotient = num // divisor
    return len(str(quotient)) == half_digits


def main():
    with open("input.txt", "r") as file:
        total_sum = 0

        ranges = file.readline().strip()
        ranges_list = parse_ranges(ranges)

        for ids_range in ranges_list:
            for i in range(ids_range[0], ids_range[1] + 1):
                if is_invalid_id(i):
                    total_sum += i

        print(total_sum)


main()
