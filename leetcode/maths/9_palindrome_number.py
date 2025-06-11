#problem link: https://leetcode.com/problems/palindrome-number/
# Approach: Reverse the number and compare it with the original number
# Time Complexity: O(log n) where n is the number of digits in x


def isPalindrome( x: int) -> bool:
        a2 = x
        temp = 0
        count = True 
        while x!= 0:
            temp += x%10
            temp = temp*10
            x = int(x/10)
        temp = temp/10
        if (temp == a2):return True 
        else: return False 
