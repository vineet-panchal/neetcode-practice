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

def twoSum(self, numbers, target):
  left = 0
  right = len(numbers) - 1

  while left < right:
    currSum = numbers[left] + numbers[right]
    if currSum > target: 
      right -= 1
    elif currSum < target:
      left += 1
    else:
      return [left + 1, right + 1]
  return []
# Time complexity: O(n)
# Space complexity: O(1)
# The time complexity is O(n) because we are iterating through the array once with two pointers, and the space complexity is O(1) because we are using only a constant amount of extra space for the left and right pointers.

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