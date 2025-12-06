def main():
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

        numbers = []
        for i in range(len(lines) - 1):
            row = [int(x) for x in lines[i].split()]
            numbers.append(row)

        operations = lines[-1].split()
        matrix = numbers

        n = len(matrix[0])

        print("Matrix:")
        for row in matrix:
            # print(row)
            print(len(row))

        print("\nOperations:")
        # print(operations)
        print(len(operations))

        total = 0
        for j in range(n):
            column_values = [matrix[i][j] for i in range(len(matrix))]

            if operations[j] == "+":
                # sum of the vertical line index j
                total += sum(column_values)
            elif operations[j] == "*":
                # product of the vertical line index j
                product = 1
                for val in column_values:
                    product *= val
                total += product

        print(f"\nTotal: {total}")

main()
