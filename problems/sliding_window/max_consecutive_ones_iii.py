"""
1004. Max consecutive ones iii.

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

"""
Approach:
+ use sliding window two pointers approach L and R at the very begining
 -> r (explores the array)
+  keep track of the num of zeros
+  and the current max length of the valid window
"""


def longestOnes(nums: list[int], k: int) -> int:
    # maximun size of the max valid window
    max_window = 0
    num_zeros = 0
    l = r = 0
    while r < len(nums):
        # move r: increasing the sliding window (explore)
        if nums[r] == 0:
            num_zeros += 1

        # move l: shrink the sliding window
        while num_zeros > k:
            if nums[l] == 0:
                num_zeros -= 1
            l += 1
        max_window = max(max_window, r - l + 1)
        r += 1
    return max_window


if __name__ == "__main__":
    print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
