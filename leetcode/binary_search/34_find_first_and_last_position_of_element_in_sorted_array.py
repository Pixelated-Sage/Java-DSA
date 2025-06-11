## 34. Find First and Last Position of Element in Sorted Array
#problem link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Approach: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

def first(nums, mid , target):
    while mid>0 and nums[mid-1] == target:
        mid = mid -1
    else:
        return mid
def last(nums, hi , mid , target):
    while mid<hi and nums[mid+1] == target:
        mid = mid + 1
    else :
        return mid


class Solution:
    def searchRange(self, nums, target: int):
        lo , hi = 0 , len(nums)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            mid_number = nums[mid]

            if mid_number == target:
                return [first(nums,mid,target), last(nums,hi,mid,target)]
            elif mid_number < target:
                lo = mid +1
            elif mid_number > target:
                hi = mid-1
        return [-1,-1]
            