def main():
    point_coordinates = []
    max_area = 0
    with open("input2.txt", "r") as file:
        for line in file:
            values = line.strip().split(",")
            x, y = int(values[0]), int(values[1])
            point_coordinates.append((x, y))

    horizontal_line_pairs = {}
    vertical_line_pairs = {}

    for i, point_a in enumerate(point_coordinates):
        for j, point_b in enumerate(point_coordinates):
            if i != j:
                if point_a[0] == point_b[0]:
                    vertical_line_pairs[(point_a[0], point_a[1])] = (
                        point_b[0],
                        point_b[1],
                    )
                elif point_a[1] == point_b[1]:
                    horizontal_line_pairs[(point_a[0], point_a[1])] = (
                        point_b[0],
                        point_b[1],
                    )

    print(horizontal_line_pairs)

    for i, point_a in enumerate(point_coordinates):
        for j, point_b in enumerate(point_coordinates):
            if (i != j) and (point_a[0] != point_b[0]) and (point_a[1] != point_b[1]):
                point_same_line_with_a = horizontal_line_pairs[(point_a[0], point_a[1])]
                point_same_line_with_b = horizontal_line_pairs[(point_b[0], point_b[1])]

                if (
                    (point_a[0] >= point_b[0] and point_a[0] <= point_same_line_with_b[0])
                    or (point_a[0] <= point_b[0] and point_a[0] >= point_same_line_with_b[0])
                ) and (
                    (point_b[0] >= point_a[0] and point_b[0] <=point_same_line_with_a[0])
                    or (point_b[0] <= point_a[0] and point_b[0] >= point_same_line_with_a[0])
                ):
                    current_area = (abs(point_a[0] - point_b[0])+1) * (abs(point_a[1] - point_b[1])+1)
                    max_area = max(max_area, current_area)

                    print(point_a, point_b, current_area)

            # print(point_a, point_b, current_area)
    # print(point_coordinates)
    print(max_area)


main()
