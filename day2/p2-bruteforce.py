def parse_ranges(range_string):
    ranges = []
    for range_part in range_string.split(","):
        start, end = range_part.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(num):
    s = str(num)
    length = len(s)

    for pattern_len in range(1, length // 2 + 1):
        # Check if length is divisible by pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]

            # Check if repeating the pattern gives the full number
            if pattern * (length // pattern_len) == s:
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
