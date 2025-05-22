"""
1. Iterative approach

Time: O(log(n))
Space: O(1)

Tip:
+ use mid = low + (high - low)// 2 to avoid float point overflow for big numbers
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


"""
Recursive approach

Best Case: O(1)
Average Case: O(log N)
Worst Case: O(log N)

Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(logN)
"""


def binarySearchRecursive(nums: list[int], target: int) -> int:
    return binarySearchRecursive_aux(nums, target, 0, len(nums) - 1)


def binarySearchRecursive_aux(nums: list[int], target: int, low: int, high: int) -> int:
    if high >= low:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            # low = mid + 1
            return binarySearchRecursive_aux(nums, target, mid + 1, high)
        elif nums[mid] > target:
            # high = mid - 1
            return binarySearchRecursive_aux(nums, target, low, mid - 1)
        else:
            return mid
    return -1


if __name__ == "__main__":
    print(binarySearch([-1, 0, 3, 5, 9, 12], 9))
    print(
        binarySearchRecursive(
            [-1, 0, 3, 5, 9, 12],
            9,
        )
    )
