"""
1. Selection Sort

The algorithm repeatedly selects the smallest (or largest) element from the unsorted
portion of the list and swaps it with the first element of the unsorted part. This
process is repeated for the remaining unsorted portion until the entire list is
sorted. time comp: O(n²) ; space comp (Auxiliary space): O(1)

TODO: fast/slow two pointers technique?
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
2. Buble Sort

+ repeatedly swapping the adjacent elements if they are in the wrong order
+ the highest will buble its way to the right with each iteration a sorted partitio
for big number wil form at the end of the array
    |-> that's why nested loop is until n - i
+ El bucle externo va hasta el n - 1 para evitar error the out of index
"""


def bubleSort(arr: list[int]) -> list[int]:
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < n - 1:
            if arr[i] > arr[i + 1]:
                swapped = True
                aux = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = aux
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


if "__main__" == __name__:
    lst1 = [99, 0, 5, 20, 123, 0, -1, 72, 21, 22, 13, 8, 7, 67, 29, 1, 2, 4]
    print(selectionSort([64, 25, 12, 22, 11]))
    print(bubleSort(lst1))
    print(insertionSort(lst1))
