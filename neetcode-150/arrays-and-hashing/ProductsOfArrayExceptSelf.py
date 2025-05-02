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

def productExceptSelf(nums):
  result = [1] * (len(nums))
  prefix = 1
  for i in range(len(nums)):
    result[i] = prefix
    prefix *= nums[i]
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