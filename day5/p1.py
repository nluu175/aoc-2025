def main():
    ranges = []
    nums = []

    with open("input.txt", "r") as file:
        for line in file:
            line_text = line.strip()
            if (line_text == ""):
                continue

            underscore_pos = line_text.find("-")
            if underscore_pos == -1:
                nums.append(int(line_text))
            else:
                ranges.append((int(line_text[:underscore_pos]), int(line_text[underscore_pos+1:])))

    fresh_count = 0
    for num in nums:
        for start, end in ranges:
            if start <= num <= end:
                fresh_count += 1
                break

    print(fresh_count)

main()
