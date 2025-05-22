def quick_sort(lst,left,right):
    #caso base: la sección the la lista que estamos trabajando solo contiene un elemento
    #o es vacia
    
    if left>=right:
        return 
    else:
        pivot=qs_partition(lst,left,right)
        quick_sort(lst,left,pivot-1)
        quick_sort(lst,pivot+1,right)


def qs_partition(lst,left,right):
    "Function to find the partition position"

    
    # choose the rightmost element as pivot
    pivot = lst[right]

    # pointer for greater element
    i = right - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(left, right):
        if lst[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (lst[i], lst[j]) = (lst[j], lst[i])
    
    # Swap the pivot element with the greater element specified by i
    (lst[i + 1], lst[right]) = (lst[right], lst[i + 1])
 
    # Return the position from where partition is done (new pivot)
    return i + 1

if "__main__" == __name__:
    arr = [12, 11, 13, 5, 6]
    print(arr)
    print(quick_sort(arr,0,len(arr)-1))


    """
    def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

    alist = [54,26,93,17,77,31,44,55,20]
    print(quicksort(alist))


    def partition(low,high,a):
    pivot=a[high]
    i=low-1
    for j in range(low,high):
      if a[j]<pivot :
        i+=1
        t=a[i]
        a[i]=a[j]
        a[j]=t
    t=a[i+1]
    a[i+1]=a[high]
    a[high]=t
    return i+1
    
    
def quickSort(low,high,arr):
    if(low<high):
        p = partition(low,high,arr)
        quickSort(low,p-1,arr)
        quickSort(p+1,high,arr)
    """