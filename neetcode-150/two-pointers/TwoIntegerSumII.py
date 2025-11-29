# 167 - Two Sum II Input Array Is Sorted
# Leetcode Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

'''
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation: The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
'''

# Solutions To The Problem:
# Time complexity: O(n)
# Space complexity: O(1)
def twoSum(numbers, target):
  left = 0 # set left pointer to the start of the list
  right = len(numbers) - 1 # set right pointer to the end of the list

  while left < right: # while left is less than right (they cannot be the same element)
    currSum = numbers[left] + numbers[right] # calculate the sum of left element and right element
    if currSum > target: 
    # if the current sum is greater than the target, then lower our bigger number (right)
      right -= 1 # then, decrement right pointer
    elif currSum < target:
    # if the current sum is less than the target, then increase our smaller number (left)
      left += 1 # then, increment left pointer
    else: # else, the current sum is equal to the target
      return [left + 1, right + 1] # return our two indices (1-indexed, so add 1 to both)
  return [] # we have not found a two sum, return empty list

if __name__ == "__main__":
  numbers = [1,2,3,4]
  target = 3
  print(twoSum(numbers, target)) # Output: [1,2]
  numbers = [1,2,3,4]
  target = 5
  print(twoSum(numbers, target)) # Output: [1,3]
  numbers = [1,2,3,4]
  target = 6
  print(twoSum(numbers, target)) # Output: [2,4]