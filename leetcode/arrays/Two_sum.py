#problem: Two Sum
#problem link: https://leetcode.com/problems/two-sum/
#approach: Hash Map


def twoSum(nums, target ):
   num_to_index = {}
   
   for i, num in enumerate(nums):
       complement = target - num
       if complement in num_to_index:
           return [num_to_index[complement], i]
       num_to_index[num] = i
   return []

        