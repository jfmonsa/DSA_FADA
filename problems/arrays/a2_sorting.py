"""
1. Selection Sort
+ current_item arr[i], current_minimum (key)
+ swap the current_item with current minimum
+ tener una particion ordenada y otra desordenada, ir iterando en la parte desordenada
    el menor el elemento swappea el actual
sorted. time comp: O(n²) ; space comp (Auxiliary space): O(1)
"""


def selectionSort(arr: list[int]) -> list[int]:
    n = len(arr)
    i = 0
    while i < n - 1:
        key = i
        j = i + 1
        while j < n:
            if arr[key] > arr[j]:
                key = j
            j += 1
        arr[key], arr[i] = arr[i], arr[key]
        i += 1
    return arr


"""
2. Bubble Sort

+ repeatedly swapping the adjacent elements if they are in the wrong order
+ a sort partition will form at the end of the array
    |-> that's why nested loop is until n - 1
+ tip: use swapped variable approach

"""


def bubbleSort(arr: list[int]) -> list[int]:
    swapped = True
    while swapped:
        swapped = False
        i = 1
        while i < len(arr):
            if arr[i - 1] > arr[i]:
                swapped = True
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i += 1
    return arr


"""
3. Insertion Sort

1. Work left or rigth
2. Examine each item and compare it to items on its left
3. insert the item in the correct position in the array
time O(n²) ; aux space O(1)
"""


def insertionSort(arr: list[int]) -> list[int]:
    # Start with the second element thus the 1st is already considered ordered
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        # move the elements that are greater than current
        # one position beyond of its current position
        # (making room for the current)
        while j > 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


"""
4. Counting Sort

0. min y max elements to create count_arr of m size m = max-min+1
1. dos arrays auxiliares count_arr y output
2. cumulative sum  in count_arr. each value marks the final index of a certain value
3. iterate from n-1 to 0 in input array and output[count_arr[index]-1] where index = arr[i]-min_elm
    and decrease count_arr[index]-=1
-> Note: We iterate from Right to Left in the sorting steps in order to guarantee the algorithm stability
    keep the relative order of the elements with equal values
"""


def countingSort(arr):
    n = len(arr)
    # min and max
    if n <= 1:
        return arr
    min_elm = max_elm = arr[0]
    for i in range(1, n):
        if arr[i] < min_elm:
            min_elm = arr[i]
        if arr[i] > max_elm:
            max_elm = arr[i]
    # count
    k = max_elm - min_elm + 1
    count_arr = [0] * k
    for i in range(n):
        count_arr[arr[i] - min_elm] += 1

    # cumulative sum
    for i in range(1, k):
        count_arr[i] += count_arr[i - 1]

    # sort
    output_arr = [0] * n
    for i in range(n - 1, -1, -1):
        index = arr[i] - min_elm
        output_arr[count_arr[index] - 1] = arr[i]
        count_arr[index] -= 1
    return output_arr


if "__main__" == __name__:
    lst1 = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    print(selectionSort([64, 25, 12, 22, 11]))
    print(bubbleSort(lst1))
    print(countingSort([2, 5, 3, 0, 2, 3, 0, 3]))
    print(countingSort([1, 4, 1, 2, 7, 5, 2]))
