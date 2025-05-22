"""
Leetcode Move Zeros

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Approach:
Tip: two pointers: fast/slow approach
1. if l != 0, go forward
2. if r ==0, go forward and check for a non-zero value
3. else: swap

zeros will go to the end
"""


def moveZeros(nums):
    n = len(nums)
    # base case
    if n < 2:
        return nums
    l = 0
    r = 1
    while r < n:
        if nums[l] != 0:
            r += 1
            l += 1
        elif nums[r] == 0:
            r += 1
        else:
            nums[l], nums[r] = nums[r], nums[l]
    return nums


if __name__ == "__main__":
    print(moveZeros([0, 1, 2, 0, 0, 3, 12]))
