'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
'''

def threeSum(self, nums):
  res = []
  nums.sort()

  for i, a in enumerate(nums):
    if i > 0 and a == nums[i - 1]:
      continue
            
    left = i + 1
    right = len(nums) - 1

    while left < right: 
      threeSum = a + nums[left] + nums[right]
      if threeSum > 0:
        right -= 1
      elif threeSum < 0:
        left += 1
      else: 
        res.append([a, nums[left], nums[right]])
        left += 1
        while nums[left] == nums[left - 1] and left < right:
          left += 1
  return res