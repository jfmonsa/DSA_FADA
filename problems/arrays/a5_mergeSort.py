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
Approach 2: indexes
"""
"""
def mergeSort_ap2(arr:list[int])->list[int]:
    if len(arr)<=0:
        return None
    return mergeSort_ap2_aux(0,len(arr)-1,arr)

def mergeSort_ap2_aux(i,j,arr):
    if i == j:
        return arr[i]
    mid = (i+j)//2

    # sort the first and second halves
    mergeSort_ap2_aux(i,mid,arr)
    mergeSort_ap2_aux(mid+1,j,arr)
    merge_ap2(arr,start,mid,end)

def merge_ap2(arr,start,mid,end):

"""


if __name__ == "__main__":
    print(mergeSort_ap1([84, 23, 29, 19, 71, 62, 63, 57]))
