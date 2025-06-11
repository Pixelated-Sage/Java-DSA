# Leetcode 74. Search a 2D Matrix
# Problem Link: https://leetcode.com/problems/search-a-2d-matrix/
# Approach: Binary Search
# Time Complexity: O(log(m*n)) where m is the number of rows and n is the number of columns
# Space Complexity: O(1)



class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        y_lo , y_hi = 0 , len(matrix)-1
        while y_lo <= y_hi:
            ex_mid = (y_lo+y_hi)//2
            row = matrix[ex_mid]
            if row[0] <= target <= row[-1]:
                x_lo , x_hi = 0 , len(row)-1
                while x_lo <=x_hi:
                    in_mid = (x_lo+x_hi)//2
                    mid_num = row[in_mid]
                    if mid_num == target:
                        return True
                    elif mid_num < target:
                        x_lo = in_mid + 1
                    else:
                        x_hi = in_mid-1
                return False
            elif target < matrix[ex_mid][0]:
                y_hi = ex_mid-1
            else :
                y_lo = ex_mid + 1
        return False 