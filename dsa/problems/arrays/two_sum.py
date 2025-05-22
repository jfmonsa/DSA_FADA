"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

"""
Aproach 1: Brute force O(n²)
+ check every pair of numbers

Aproach 2: use a hashmap O(n)
1 save the index (value) of each element (key) in a hashmap
2 use b = target - a to come up with the second element
"""


def twoSum(nums, target):
    aux = {}
    for i in range(len(nums)):
        aux[nums[i]] = i
    for i in range(len(nums)):
        # nums[i] is a
        # target - nums[i] is b
        b = target - nums[i]
        if b in aux and i != aux[b]:
            return [i, aux[b]]


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
