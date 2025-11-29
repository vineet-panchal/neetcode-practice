# 238 - Product of Array Except Self
# Leetcode Link: https://leetcode.com/problems/product-of-array-except-self/

'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
'''

'''
Initial Thoughts

Simplify the problem:
  - given an array, we are to return an array where each element of the resulting array is the product of all the elements except itself

Pattern Recognition: Straightforward/Optimal solution
  - we can use a two pass approach, where the first pass builds up the product of all elements before each index
  - the second pass, multiplies each position of all elements after that index
'''

# Solutions To The Problem:

# Two-Pass Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def productExceptSelf(nums):
  '''
  we can use the two pass-approach
  the first pass, builds up the product of all elements before each index
  the second pass, multiplies each position of all elements after that index
  
  Let's trace through with nums = [1, 2, 3, 4]:
  After initialization:
  result = [1, 1, 1, 1]
  First loop (prefix products):
  i=0: result[0] = 1,      prefix = 1 → 1   | result = [1, 1, 1, 1]
  i=1: result[1] = 1,      prefix = 1 → 2   | result = [1, 1, 1, 1]
  i=2: result[2] = 2,      prefix = 2 → 6   | result = [1, 1, 2, 1]
  i=3: result[3] = 6,      prefix = 6 → 24  | result = [1, 1, 2, 6]
  Second loop (postfix products):
  i=3: result[3] = 6 * 1 = 6,    postfix = 1 → 4   | result = [1, 1, 2, 6]
  i=2: result[2] = 2 * 4 = 8,    postfix = 4 → 12  | result = [1, 1, 8, 6]
  i=1: result[1] = 1 * 12 = 12,  postfix = 12 → 24 | result = [1, 12, 8, 6]
  i=0: result[0] = 1 * 24 = 24,  postfix = 24 → 24 | result = [24, 12, 8, 6]
  '''
  result = [1] * (len(nums)) # initialize result list
  # first pass
  prefix = 1 # set prefix to 1, to multiply
  for i in range(len(nums)):
    result[i] = prefix
    prefix *= nums[i]
  
  # second pass
  postfix = 1
  for i in range(len(nums) - 1, -1, -1):
    result[i] *= postfix
    postfix *= nums[i]
  return result

# Time complexity: O(n)
# Space complexity: O(1) (excluding the output array)

if __name__ == "__main__":
  # Test cases
  print(productExceptSelf([1,2,4,6])) # [48,24,12,8]
  print(productExceptSelf([-1,0,1,2,3])) # [0,-6,0,0,0]
  print(productExceptSelf([1])) # [1]
  print(productExceptSelf([1,2])) # [2,1]
  print(productExceptSelf([1,2,3])) # [6,3,2]