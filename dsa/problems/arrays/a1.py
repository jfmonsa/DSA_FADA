# 1. Find Largest Three Elements
def largest3(arr: list[int, float]) -> tuple[int, float]:
    first = second = third = float("-inf")

    i = 0
    while i < len(arr):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second:
            third = second
            second = arr[i]
        elif arr[i] > third:
            third = arr[i]
        i += 1
    return (first, second, third)


if "__main__" == __name__:
    print(largest3([6, 8, 1, 9, 2, 1, 10, 10]))
