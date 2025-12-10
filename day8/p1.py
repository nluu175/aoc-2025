# Some observations:
# - We count attempts instead of sucessful connections
# - This looks like a Minimum Spanning Tree, thus Kruskal can be used (thank god I did take Graph Theory at school :P)

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

    # Process first 1000 attempts
    for idx in range(1000):
        dist, i, j = distances[idx]
        union(parent, i, j)

    circuit_sizes = {}
    for i in range(len(point_coordinates)):
        root = find(parent, i)
        if root not in circuit_sizes:
            circuit_sizes[root] = []
        circuit_sizes[root].append(i)

    sizes = sorted([len(members) for members in circuit_sizes.values()], reverse=True)

    print(f"Circuit sizes: {sizes}")
    print(f"Number of circuits: {len(sizes)}")
    print(f"Product of three largest: {sizes[0] * sizes[1] * sizes[2]}")

main()
