import time
def delay():
    time.sleep(2)

def searchMatrix(matrix, target):

    y_lo, y_hi = 0, len(matrix) - 1
    while y_lo <= y_hi:
        ex_mid = (y_lo + y_hi) // 2
        row = matrix[ex_mid]
        if row[0] <= target <= row[-1]:
            x_lo, x_hi = 0, len(row) - 1
            while x_lo <= x_hi:
                in_mid = (x_lo + x_hi) // 2
                mid_num = row[in_mid]
                if mid_num == target:
                    return True
                elif mid_num < target:
                    x_lo = in_mid + 1
                else:
                    x_hi = in_mid - 1
            return False
        elif target < row[0]:
            y_hi = ex_mid - 1
        else:
            y_lo = ex_mid + 1
    return False


# Example usage:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
result = searchMatrix(matrix, target)
print(f"Target {target} found: {result}")