def main():
    point_coordinates = []
    max_area = 0
    with open("input.txt", "r") as file:
        for line in file:
            values = line.strip().split(',')
            x, y = int(values[0]), int(values[1])
            point_coordinates.append((x, y))

    for i, point_a in enumerate(point_coordinates):
        for j, point_b in enumerate(point_coordinates):
            if (i != j) and (point_a[0] != point_b[0]) and (point_a[1] != point_b[1]):
                current_area = (abs(point_a[0] - point_b[0])+1) * (abs(point_a[1] - point_b[1])+1)
                max_area = max(max_area, current_area)

                # print(point_a, point_b, current_area)
    # print(point_coordinates)
    print(max_area)


main()
