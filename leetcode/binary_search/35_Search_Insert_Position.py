# 35. Search Insert Position
# Problem Link: https://leetcode.com/problems/search-insert-position/
# Approach: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)


def searchInsert( nums, target: int) -> int:
    lo , hi = 0 , len(nums)-1
    while lo <=hi:
        mid = ((lo+hi)//2)
        mid_number = nums[mid]
        if mid_number == target:
            return mid
        elif mid_number < target:
            lo = mid+1
        elif mid_number > target:
            hi = hi-1
        else :
            return -1
    return hi+1