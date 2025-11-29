# 1 - Two Sum
# Leetcode Link: https://leetcode.com/problems/two-sum/

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
Initial Thoughts

Simplify the problem:
  - given a list of numbers and a target int, find two numbers whose sum is the target, and return their indcies in a list

Pattern Recognition: Straightforward solution
  - we can use loops that represent two pointers, and go through the list and find two elements that add up to the target

Pattern Recognition: Optimal solution
  - use a hashmap to keep track of what we've already seen, and their indices
  - loop through the list using enumerate to get the index and the element
  - calculate the current difference by substracting the current element from the target
  - we can then check if our difference is in our hashmap
  - if it is then return the index and the index of the element we found in the hashmap in a list
  - else we just add the element and its index into the hashmap
'''

# Solutions to the problem:

# Hashmaps
# Time complexity: O(n)
# Space complexity: O(n)
def twoSum(nums, target):
  seen = {} # keep track of the elements, and their index
  for i, num in enumerate(nums): # loop through the list, and get their index (i) and element (num)
    complement = target - num # calculate the complement, target - current element
    if complement in seen: # if the complement is in seen:
      return [seen[complement], i] # then we have found our two indices, and return it
    seen[num] = i # else put the element and its index in the hashmap
  return [] # we have found nothing



# Nested Loops
# Time complexity: O(n^2)
# Space complexity: O(1)
def twoSum2(nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
  return []

if __name__ == "__main__":
  # Test cases
  print(twoSum([3,4,5,6], 7)) # [0,1]
  print(twoSum([4,5,6], 10)) # [0,2]
  print(twoSum([5,5], 10)) # [0,1]
  print(twoSum2([3,4,5,6], 7)) # [0,1]
  print(twoSum2([4,5,6], 10)) # [0,2]
  print(twoSum2([5,5], 10)) # [0,1]
