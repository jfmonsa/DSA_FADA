"""
26. Remove duplicates from sorted array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


def removeDuplicates(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return
    l = 0
    r = 1
    while r < len(nums):
        if nums[l] == nums[r]:
            r += 1
        else:
            l += 1
            nums[l] = nums[r]
    return l + 1


if __name__ == "__main__":
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
