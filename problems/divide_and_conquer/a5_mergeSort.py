"""
Approach 1: Using arrays slincing, this is less effcient
hece we are creating a copy of the original array to create a subarray
for each call of merge sort func
"""


def mergeSort_ap1(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    sorted_left = mergeSort_ap1(left_arr)
    sorted_right = mergeSort_ap1(right_arr)

    return merge_ap1(sorted_left, sorted_right)


def merge_ap1(l: list[int], r: list[int]) -> list[int]:
    arr_result = []
    i, j = 0, 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr_result.append(l[i])
            i += 1
        else:
            arr_result.append(r[j])
            j += 1

    arr_result.extend(l[i:])
    arr_result.extend(r[j:])

    return arr_result


"""
Approach 2: Merge Sort with indexes, inplace operatiosn
"""


def mergeSort(arr):
    mergeSort_aux(arr, 0, len(arr) - 1)
    return arr


def mergeSort_aux(arr, start, end):
    # conquer
    # Note: in-place operations, thus we don't have to return anything
    if start >= end:
        return
    # divide
    mid = (start + end) // 2
    mergeSort_aux(arr, start, mid)
    mergeSort_aux(arr, mid + 1, end)
    # combine
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    # subarrays
    L = arr[start : mid + 1]
    R = arr[mid + 1 : end + 1]
    i = 0
    j = 0
    # index to the original array
    k = start
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    print(mergeSort([84, 23, 29, 19, 71, 62, 63, 57]))
    print(mergeSort([38, 27, 43, 10]))
