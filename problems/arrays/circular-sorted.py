"""
Consider an array: arr[] = {23, 34, 45, 12, 17, 19}
The elements here, {12, 17, 19, 23, 34, 45}
are sorted "In-order" but they are rotated to the left by 3 times.
"""


def check_asc_circular_sorted(lst):
    "check for an ascending circular sorted list"
    cnt=0
    n=len(lst)
            
    for i in range(1, n):
        if lst[i - 1] > lst[i]:
            cnt += 1


    if cnt == 1 and lst[0]>=lst[n-1]:
        # First condition means there is only one instance where
        # contiguous increasing condition is violated
        # mataining it's circular nature, the we further
        # check if the first element is greater or equal
        # than the last; if both conditions are true this
        # implies that the lst is circular sorted
        return True
    return False

def check_desc_circular_sorted(lst):
    cnt=0
    n=len(lst)
    for i in range(1,n):
        if lst[i-1]<lst[i]:
            cnt+=1
    
    if cnt==1 and lst[0]<=lst[n-1]:
        return True
    return False

#tests
if __name__=="__main__":
    arr1 = [23, 34, 45, 12, 17, 19]
    print(check_asc_circular_sorted(arr1))
    arr2 = [9, 5, 3, 35, 26, 11]
    print(check_desc_circular_sorted(arr2))

