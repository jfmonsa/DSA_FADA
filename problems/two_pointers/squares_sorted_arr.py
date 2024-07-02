"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Tip:
+ when squared -> two sorted subarrays will be form start (negative squared numbers) and end
+ use aux array to sort numbers with two pointers
"""


def squaresSorted(nums: list[int]) -> list[int]:
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    aux = [0] * n
    for i in range(n):
        nums[i] = nums[i] ** 2

    l = 0
    r = n - 1
    i = n - 1
    while i >= 0:
        if nums[l] > nums[r]:
            aux[i] = nums[l]
            l += 1
        else:
            aux[i] = nums[r]
            r -= 1
        i -= 1
    return aux


if __name__ == "__main__":
    print(squaresSorted([-4, -1, 0, 3, 10]))
