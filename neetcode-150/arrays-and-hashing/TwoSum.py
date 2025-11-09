'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]
'''

'''
Step 1: given a list of numbers and a target value, find the index of two numbers in the list where the sum is the target, the indices cannot be the same.
Step 2: We can just go through the given list, and find values where the sum is the target.
Straightforward: 
Use two loops to go through the list. Start the second loop should start after the index of the first. Find values where the sum is equal to target, and return their indices.
Optimal:
Use a hashmap to remember what we already seen and their indices
'''

# solution 1
def twoSum(nums, target):
  seen = {} # keep track of the elements, and their index
  for i, num in enumerate(nums): # loop through the list, and get their index (i) and element (num)
    complement = target - num # calculate the complement, target - current element
    if complement in seen: # if the complement is in seen:
      return [seen[complement], i] # then we have found our two indices, and return it
    seen[num] = i # else put the element and its index in the hashmap
  return [] # we have found nothing
# Time complexity: O(n)
# Space complexity: O(n)

# solution 2
def twoSum2(nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
  return []
# Time complexity: O(n^2)
# Space complexity: O(1)

if __name__ == "__main__":
  # Test cases
  print(twoSum([3,4,5,6], 7)) # [0,1]
  print(twoSum([4,5,6], 10)) # [0,2]
  print(twoSum([5,5], 10)) # [0,1]
  print(twoSum2([3,4,5,6], 7)) # [0,1]
  print(twoSum2([4,5,6], 10)) # [0,2]
  print(twoSum2([5,5], 10)) # [0,1]
