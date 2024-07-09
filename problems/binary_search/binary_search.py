"""

Tip:
+ use mid = low (high - low)// 2 to avoid float point overflow for big numbers
+ two pointers approach
"""


def binarySearch(nums: list[int], target: int) -> int:

    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target < nums[mid]:
            # search backwards
            high = mid - 1
        elif target > nums[mid]:
            # search fordwards
            low = mid + 1
        else:
            # return the index of target
            return mid
    return -1


if __name__ == "__main__":
    print(binarySearch([-1, 0, 3, 5, 9, 12], 9))
