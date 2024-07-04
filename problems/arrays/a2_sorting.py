"""
1. Selection Sort
+ current_item arr[i], current_minimum (key)
+ swap the current_item with current minimum
+ tener una particion ordenada y otra desordenada, ir iterando en la parted desordenada
    el menor el elemento swappea el actual
sorted. time comp: O(n²) ; space comp (Auxiliary space): O(1)
"""


def selectionSort(arr: list[int]) -> list[int]:
    i = 0
    while i < len(arr):
        minIdx = i
        j = i + 1
        while j < len(arr):
            if arr[minIdx] > arr[j]:
                minIdx = j
            j += 1
        current = arr[i]
        arr[i] = arr[minIdx]
        arr[minIdx] = current
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
        i = 0
        while i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                # swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
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
"""


def countingSort(arr: list[int]) -> list[int]:

    n = len(arr)
    # find max and min
    min_elm = min(arr)
    max_elm = max(arr)

    # initialize coutring arr (+1 for 0-index)
    m = max_elm - min_elm + 1
    count_arr = [0] * (m)

    # Couting occurrences
    for elm in arr:
        count_arr[elm] += 1

    # cumulative sum
    # Modify count_arr
    # para que cada elemento en la posición $i$ contenga la suma de los conteos anteriores.
    # Esto permite determinar la posición final de cada elemento en el array ordenado.
    # countArray[i] = countArray[i – 1] + countArray[i].

    for i in range(1, m):
        count_arr[i] += count_arr[i - 1]

    for i in range(n):
        arr[i]


if "__main__" == __name__:
    lst1 = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    print(selectionSort([64, 25, 12, 22, 11]))
    print(bubbleSort(lst1))
