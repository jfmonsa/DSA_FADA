"""
Leetcode 167: Two sum II - input arr sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
ind two numbers such that they add up to a specific target number. Let these two numbers be
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array
[index1, index2] of length 2.
"""


def twoSumSorted(nums: list[int], target: int) -> list[int]:
    l = 0
    r = len(nums) - 1
    while l < r:
        summ = nums[l] + nums[r]
        if summ < target:
            l += 1
        elif summ > target:
            r -= 1
        else:
            # if target = summ
            return [l + 1, r + 1]


if __name__ == "__main__":
    print(twoSumSorted([2, 7, 11, 15], 9))
