# Some observations
# - can do by math like in p1 but will be a bit different
# - 1212 is divivded by 101
# - 121212 is divided by 10101
# - All of them follows this pattern


def parse_ranges(range_string):
    ranges = []
    for range_part in range_string.split(","):
        start, end = range_part.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(num):
    s = str(num)
    length = len(s)

    # Try all possible pattern lengths (from 1 to length//2)
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            num_repeats = length // pattern_len

            # Calculate divisor: sum of powers of 10^pattern_len
            # For pattern_len=3, repeats=3: 10^6 + 10^3 + 1 = 1001001
            # For pattern_len=2, repeats=5: 10^8 + 10^6 + 10^4 + 10^2 + 1
            divisor = 0
            for i in range(num_repeats):
                divisor += 10 ** (i * pattern_len)

            if num % divisor == 0:
                quotient = num // divisor
                if len(str(quotient)) == pattern_len:
                    return True

    return False


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
