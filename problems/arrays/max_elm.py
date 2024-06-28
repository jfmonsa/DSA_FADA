"""
1. Using divide and conquer, find the maximun element
of an arra
"""


def max_elm(arr: list[int]) -> int:
    n = len(arr)
    # handle edge case: empty list
    if n == 0:
        return None
    """
    We start with a subarray arr[0:n]
    """
    return max_elm_aux(0, n - 1, arr)


def max_elm_aux(i, j, arr):
    """
    Approach:

    i <- pointer to the starting position of the portion of
    the array (start index of subarray)
    j <- pointer to the end position of portion of the
    array (end position of subarray)

    Note: we work with indexes, then we don't have to make a copy
    of the original array

    if i == j --> means we have a subarray of only one elm
    """
    # conquer or base case
    if i == j:
        return arr[i]
    # divide
    # -> use // operator to avoid floating-point division
    mid = (i + j) // 2
    # combine solutions (max function)
    return max(max_elm_aux(i, mid, arr), max_elm_aux(mid + 1, j, arr))


"""
2. Modify the previous algo to return the minimun value in a three way search
(Divide and conquer)
"""


def min_elm(arr: list[int]) -> int:
    n = len(arr)
    if n == 0:
        return None
    return min_elm_aux(0, n - 1, arr)


def min_elm_aux(i, j, arr):
    # conquer
    # This prevents the division into thirds when there are not enough elements.
    if i == j:
        return arr[i]
    elif j - i == 1:
        return min(arr[i], arr[j])
    # divide
    third = (j - i + 1) // 3
    q1 = i + third - 1
    q2 = j - third + 1

    # combine
    return min(
        min_elm_aux(i, q1, arr),
        min_elm_aux(q1 + 1, q2 - 1, arr),
        min_elm_aux(q2, j, arr),
    )


if __name__ == "__main__":
    print(max_elm([2, 1, 0, -4, 3, 6, 7, 5]))
    print(min_elm([2, 1, 0, -4, 3, 6, 7, 5]))
