# In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
# In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
# In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
# In 818181911112111, the largest joltage you can produce is 92.
#
# Notes:
# - Order has to be maintained
# - The idea is we add everything to a stack (since order is always maintained)
# then pop the stack when we reach a satisfying condition


def get_largest_number(digits: str, no_digits: int) -> str:
    n = len(digits)
    to_remove = n - no_digits
    stack = []

    for i, digit in enumerate(digits):
        remaining = n - i
        # Only remove if we'll still have enough digits to reach length k
        while (
            len(stack) > 0
            and stack[-1] < digit
            and to_remove > 0
            and len(stack) - 1 + remaining > no_digits  # Do we have enough digits to reach out target length (aka. no_digits)
        ):
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    # If we haven't removed enough, remove from end
    while to_remove > 0:
        stack.pop()
        to_remove -= 1

    return "".join(stack)


def main():
    with open("input.txt", "r") as file:
        sum = 0
        for line in file:
            print(line)
            a = get_largest_number(line, 12)
            print(a)
            sum += int(a)

        print(sum)


main()
