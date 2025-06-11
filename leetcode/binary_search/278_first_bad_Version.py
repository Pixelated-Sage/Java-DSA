# 278. First Bad Version
#problem link: https://leetcode.com/problems/first-bad-version/
# Approach: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

#making a temp.. isBadVersion function to simulate the API call

def isBadVersion(version: int) -> bool:
    # This is a placeholder for the actual implementation of the isBadVersion API.
    # In a real scenario, this function would be provided by the problem environment.
    pass

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def test(mid):
    if isBadVersion(mid):
        if mid > 1 and isBadVersion(mid-1):
            return 'left'
        return 'found'
    elif not isBadVersion(mid):
        return 'right'

class Solution:


    def firstBadVersion(self, n: int) -> int:
        lo , hi = 1 , n
        while lo <=hi:
            mid = (lo+hi)//2
            result = test(mid)
            if result == 'found':
                return (mid)
            elif result == 'left':
                hi = mid -1
            elif result == 'right':
                lo = mid + 1    