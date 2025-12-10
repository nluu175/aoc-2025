# Some observations:
# - We count attempts instead of sucessful connections

import math

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return False

    parent[root_x] = root_y
    return True

def get_distance_between_2_points(point_a, point_b):
    distance = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2 + (point_a[2] - point_b[2])**2)
    return distance

def main():
    point_coordinates = []
    with open("input.txt", "r") as file:
        for line in file:
            values = line.strip().split(',')
            x, y, z = int(values[0]), int(values[1]), int(values[2])
            point_coordinates.append((x, y, z))

    distances = []
    for i, point_a in enumerate(point_coordinates):
        for j, point_b in enumerate(point_coordinates):
            if i < j:
                dist = get_distance_between_2_points(point_a, point_b)
                distances.append((dist, i, j))

    distances.sort()

    parent = list(range(len(point_coordinates)))

    # Keep track of number of separate circuits
    num_circuits = len(point_coordinates)
    last_connection = None

    # Process until all are in one circuit
    for idx in range(len(distances)):
        dist, i, j = distances[idx]
        if union(parent, i, j):
            num_circuits -= 1
            last_connection = (i, j)
            if num_circuits == 1:
                break

    if last_connection:
        i, j = last_connection
        print(f"Last connection: {point_coordinates[i]} and {point_coordinates[j]}")
        x_product = point_coordinates[i][0] * point_coordinates[j][0]
        print(f"X coordinates: {point_coordinates[i][0]} * {point_coordinates[j][0]} = {x_product}")

main()
