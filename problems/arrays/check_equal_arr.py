"""
Given two arrays, arr1 and arr2 of equal length N, the task
is to find if the given arrays are equal or not. 

Two arrays are said to be equal if:
* both of them contain the same set of elements, 
* arrangements (or permutations) of elements might/might not be same.
* If there are repetitions, then counts of repeated elements must also
be the same for two arrays to be equal.
"""

def check_equal_lst(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    if n1!=n2:
        return False
    dict1 = {}

    #filling the hash map
    for i in range(0,n1):
        dict1[str(arr1[i])] = dict1.get(i, 0) + 1
        dict1[str(arr2[i])] = dict1.get(i, 0) - 1

    #if all the values of the keys in the hashmap
    #are 0, both arrays are equal according to the
    #the given rules
    for value in dict1.values():
        if value!=0:
            return False
    return True

if "__main__" == __name__:
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]
    
    print(check_equal_lst(arr1,arr2))
    
        

