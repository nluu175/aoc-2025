def is_rect_valid_compressed(prefix, x1_idx, y1_idx, x2_idx, y2_idx):
    """Check if rectangle is all valid in compressed coordinates"""
    # Building: Each cell = current + top + left - overlap
    # Querying: Total area - top excess - left excess + corner correction

    # count = (prefix[x2+1][y2+1] -         # Everything up to (x2,y2)
    #      prefix[x1][y2+1] -               # Subtract top rectangle
    #      prefix[x2+1][y1] +               # Subtract left rectangle
    #      prefix[x1][y1])                  # Add back corner (counted twice)

    min_x = min(x1_idx, x2_idx)
    max_x = max(x1_idx, x2_idx)
    min_y = min(y1_idx, y2_idx)
    max_y = max(y1_idx, y2_idx)


    expected = (max_x - min_x + 1) * (max_y - min_y + 1)
    actual = (
        prefix[max_x + 1][max_y + 1]
        - prefix[min_x][max_y + 1]
        - prefix[max_x + 1][min_y]
        + prefix[min_x][min_y]
    )

    return actual == expected


def main():
    point_coordinates = []
    with open("input2.txt", "r") as file:
        for line in file:
            values = line.strip().split(",")
            x, y = int(values[0]), int(values[1])
            point_coordinates.append((x, y))

    print("All points:", point_coordinates)

    # Map actual coordinates to compressed indices
    all_x = sorted(set(p[0] for p in point_coordinates))
    all_y = sorted(set(p[1] for p in point_coordinates))

    print("All X(s):", all_x)
    print("All Y(s):", all_y)

    x_to_compressed = {x: i for i, x in enumerate(all_x)}
    y_to_compressed = {y: i for i, y in enumerate(all_y)}

    print("Compressed X(s):", x_to_compressed)
    print("Compressed y(s):", y_to_compressed)

    # Convert to compressed coordinates
    compressed_coords = [
        (x_to_compressed[x], y_to_compressed[y]) for x, y in point_coordinates
    ]

    print("Compressed Coors:", compressed_coords)

    # Build green tiles in compressed space
    green_tiles_compressed = set()

    # "Tiles that are adjacent in your list will always be on either the same row or the same column."
    # This guarantees that coordinates next to each other are either on the same row or column
    # This is why next_point is guaranteed
    for i in range(len(compressed_coords)):
        current = compressed_coords[i]
        next_point = compressed_coords[
            (i + 1) % len(compressed_coords)
        ]  # This guarantees index doesn't go out of bound at the end

        if current[0] == next_point[0]:
            # Same column
            smaller_y = min(current[1], next_point[1])
            bigger_y = max(current[1], next_point[1])
            for y_idx in range(smaller_y, bigger_y + 1):
                green_tiles_compressed.add((current[0], y_idx))
        else:
            # Same row
            smaller_x = min(current[0], next_point[0])
            bigger_x = max(current[0], next_point[0])
            for x_idx in range(smaller_x, bigger_x + 1):
                green_tiles_compressed.add((x_idx, current[1]))

    print("Outer Green Titles:", green_tiles_compressed)

    # Build vertical edges in compressed space. These vertical edges are used for ray-casting the coordinate horizontally
    vertical_edges = {}
    for i in range(len(compressed_coords)):
        # Similar to above, p1 and p2 are adjacent due to the contraint in the problem
        p1 = compressed_coords[i]
        p2 = compressed_coords[(i + 1) % len(compressed_coords)]

        if p1[0] == p2[0]:  # Vertical edge
            edge_x = p1[0]
            min_edge_y = min(p1[1], p2[1])
            max_edge_y = max(p1[1], p2[1])
            if edge_x not in vertical_edges:
                vertical_edges[edge_x] = []
            vertical_edges[edge_x].append((min_edge_y, max_edge_y))

    print("Vertical Edges:", vertical_edges)

    # Find interior points using ray casting
    width = len(all_x)
    height = len(all_y)

    # x_idx and y_idx denote the index while edge_x is the x coordinate of the vertical edge.
    # since we're looking at the compressed coordinates, x_idx and edge_x have the same meaning
    for x_idx in range(width):
        for y_idx in range(height):
            if (x_idx, y_idx) in green_tiles_compressed:
                continue

            intersections = 0
            for edge_x, edges in vertical_edges.items():
                if (
                    edge_x > x_idx
                ):  # only count vertical edges to the right of the current point
                    for min_edge_y, max_edge_y in edges:
                        if min_edge_y <= y_idx < max_edge_y:
                            intersections += 1

            # Ray Casting
            # - if #intersection is odd (mod2==1) -> the point is inside the polygon
            # - if #intersection is even (mod2==0) -> the point is outside the polygon
            if intersections % 2 == 1:
                green_tiles_compressed.add((x_idx, y_idx))

    red_tiles_compressed = set(compressed_coords)
    valid_tiles_compressed = red_tiles_compressed | green_tiles_compressed

    # Build grid in compressed space which is used for building the prefix sum
    grid = [[0] * height for _ in range(width)]
    for x_idx, y_idx in valid_tiles_compressed:
        grid[x_idx][y_idx] = 1

    # Build 2D prefix sum that count the number of valid titles (red or green)
    # prefix[i][j] = total count of valid tiles in rectangle from (0,0) to (i-1, j-1)
    # - grid[i][j]: current cell
    # - prefix[i][j + 1]: rectangle above
    # - prefix[i + 1][j]: rectangle on the left
    # - prefix[i][j]: overlap
    prefix = [[0] * (height + 1) for _ in range(width + 1)]
    for i in range(width):
        for j in range(height):
            prefix[i + 1][j + 1] = (
                grid[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
            )

    # Find maximum area
    max_area = 0
    max_rect = None

    # Build all possible pairs sorted by potential area
    pairs = []
    for i in range(len(point_coordinates)):
        point_a = point_coordinates[i]
        compressed_a = compressed_coords[i]

        for j in range(i + 1, len(point_coordinates)):
            point_b = point_coordinates[j]
            compressed_b = compressed_coords[j]

            # Skip if same row or column as we only get pair from opposite corners of the rectangle
            if compressed_a[0] == compressed_b[0] or compressed_a[1] == compressed_b[1]:
                continue

            # Calculate ACTUAL area (aka. with orginal coordinates)
            actual_area = (abs(point_a[0] - point_b[0]) + 1) * (
                abs(point_a[1] - point_b[1]) + 1
            )
            pairs.append(
                (actual_area, i, j, compressed_a, compressed_b, point_a, point_b)
            )

    # Pairs is constructed in this structure [actual_area, index_a, index_b, compressed_a, compressed_b, point_a, point_b]
    print("Pairs:", pairs)

    # Sort the pairs by area and desc order. Doing it this way, we can get the max rectangle early
    pairs.sort(reverse=True, key=lambda x: x[0])

    # Check rectangles
    for actual_area, i, j, compressed_a, compressed_b, point_a, point_b in pairs:
        if actual_area <= max_area:
            break

        # Validate by comparing the actual area vs. the number of valid titles in the rectangle
        if is_rect_valid_compressed(
            prefix, compressed_a[0], compressed_a[1], compressed_b[0], compressed_b[1]
        ):
            max_area = actual_area
            max_rect = (point_a, point_b)
            print(f"Found valid rectangle with area {max_area}: {point_a} to {point_b}")

    if max_rect:
        print(
            f"Rectangle corners: {max_rect[0]} and {max_rect[1]} form a rectangle with Maximum area of {max_area}"
        )


main()
