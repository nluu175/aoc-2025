def main():
    ranges = []

    with open("input.txt", "r") as file:
        for line in file:
            line_text = line.strip()
            if (line_text == ""):
                # this marks the end of the first part of the database; also we only need ranges.
                break

            underscore_pos = line_text.find("-")
            if underscore_pos != -1:
                ranges.append((int(line_text[:underscore_pos]), int(line_text[underscore_pos+1:])))


    # sort then merge overlapped ranges
    ranges.sort()
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    print(merged)

    total = 0
    for start, end in merged:
        total += end - start + 1

    print(total)

main()
