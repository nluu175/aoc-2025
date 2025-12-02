def parse_ranges(range_string):
    ranges = []
    for range_part in range_string.split(","):
        start, end = range_part.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def is_invalid_id(num):
    s = str(num)
    length = len(s)

    if length % 2 != 0:
        return False

    mid = length // 2
    return s[:mid] == s[mid:]


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
