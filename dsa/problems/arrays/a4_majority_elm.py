"""
Given an array of integer, find the majority element.

A majority element is one that occurs more than n/2 times,
where n is the total number of elements
"""


def majority_elm_ap1(arr: list[int]) -> int:
    """
    Approach 1:
    naive approach: sort it at since it has to be greater than
    n/2 the elm in the middle must be the majority elm

    O(nlog(n))
    """
    n = len(arr)
    arr.sort()  # n log n1
    return arr[n // 2]


def majority_elm_ap2(arr: list[int]) -> int:
    """
    Approach 2:
    using a hash table such as a dictionary

    time: O(n)
    aux space: O(n)
    """
    aux = {}

    for elm in arr:
        if elm in aux:
            aux[elm] = aux[elm] + 1
        else:
            aux[elm] = 1

    for key in aux.keys():
        if aux[key] > len(arr) // 2:
            return key
    # If no majority element is found
    return None


def majority_elm_ap3(arr: list[int]) -> int:
    """
    Approach 3: voting algo
    O(1) space, O(n) time
    """

    majority = arr[0]
    votes = 0
    for candidate in arr:
        if candidate == majority:
            votes += 1
        else:
            votes -= 1
            if votes == 0:
                majority = candidate
                votes += 1
    return majority


if "__main__" == __name__:
    print(majority_elm_ap2([3, 2, 3]))
    print(majority_elm_ap3([2, 2, 1, 3, 1, 2, 2]))
