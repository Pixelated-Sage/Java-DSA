# LeetCode 704. Binary Search
# Problem Link: https://leetcode.com/problems/binary-search/
# Approach: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def search(self, nums, target: int) -> int:
        lo , hi = 0 , len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            mid_number= nums[mid]
            if mid_number == target:
                return mid
            elif mid_number < target:
                lo = mid +1
            else:
                hi = mid -1
        return -1 