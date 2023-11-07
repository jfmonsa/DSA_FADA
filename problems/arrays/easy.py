from typing import List
import copy

"""
(1) Write a program to reverse an array or string
"""

def reverse_array(arr:List[any])->List[any]:
    arr_c =arr.copy()
    start=0
    end=len(arr)-1
    while start < end: 
        arr_c[start], arr_c[end] = arr_c[end], arr_c[start] #swapping values
        start += 1
        end -= 1
    else:
        print(arr)
        return arr
    
"""
#test
reverse_array([33,213,76,4,56,3,2,1])
"""

"""
(2)given an array, the task is to cyclically rotate the array
clockwise by one time. 
"""

def rotate_array(arr:List[any])->List[any]:
    
    """Right rotate an array """
    arr_c=arr.copy()
    n=len(arr)    
    last_el = arr_c[n - 1]

    for i in range(n - 1, 0, -1):
        arr_c[i] = arr_c[i - 1]
        
    arr_c[0] = last_el
    print(arr_c)
    return arr_c

"""
#test
rotate_array([1, 2, 3, 4, 5])
"""

"""
Subarray problems

Aproach, use sliding window strategic to get solutions in linear time O(n)
https://youtu.be/GcW4mgmgSbw?si=1TJGH6GFo2J1CB28

* Fixed size sliding window
* dynamically size slinding window

TODO:
(3) Largest Sum Contiguous Subarray (Kadane’s Algorithm)
"""
"""
def lagest_sum(arr:List[int])->List[int]:
    max_so_far =  INT_MIN
    max_ending_here = 0
"""