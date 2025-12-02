# Some optimizations
# - Since 11 or 101 or 1001 or 10101 etc guarantees an invalid ids, inverse the p2-math solution can save lots of times.


def parse_ranges(range_string):
    ranges = []
    for range_part in range_string.split(","):
        start, end = range_part.split("-")
        ranges.append((int(start), int(end)))
    return ranges


def generate_invalid_ids_in_range(start, end):
    invalid_ids = set()

    # For each possible pattern length
    for pattern_len in range(1, len(str(end)) + 1):
        # For each number of repeats (at least 2)
        for num_repeats in range(2, len(str(end)) // pattern_len + 2):
            # Calculate the divisor
            divisor = sum(10 ** (i * pattern_len) for i in range(num_repeats))

            # Generate invalid IDs by multiplying
            # Start from the smallest multiplier that gets us into range
            min_multiplier = max(1, (start + divisor - 1) // divisor)
            max_multiplier = end // divisor

            for multiplier in range(min_multiplier, max_multiplier + 1):
                invalid_id = multiplier * divisor

                # Check if in range and has correct number of digits (no leading zeros)
                if start <= invalid_id <= end and len(str(multiplier)) == pattern_len:
                    invalid_ids.add(invalid_id)

    return invalid_ids


def main():
    with open("input.txt", "r") as file:
        total_sum = 0

        ranges = file.readline().strip()
        ranges_list = parse_ranges(ranges)

        for ids_range in ranges_list:
            invalid_ids = generate_invalid_ids_in_range(ids_range[0], ids_range[1])
            total_sum += sum(invalid_ids)

        print(total_sum)


main()
