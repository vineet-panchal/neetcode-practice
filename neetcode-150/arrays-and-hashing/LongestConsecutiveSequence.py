'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
'''

def longestConsecutive(nums) -> int:
  numSet = set(nums)
  maxLength = 0

  for n in nums:
    if (n - 1) not in numSet:
      currLength = 0
      while (n + currLength) in numSet:
        currLength += 1
      maxLength = max(currLength, maxLength)
  return maxLength

# Time complexity: O(n)
# Space complexity: O(n)
if __name__ == "__main__":
  # Test cases
  print(longestConsecutive([2, 20, 4, 10, 3, 4, 5])) # 4
  print(longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1])) # 7
  print(longestConsecutive([1, 2, 3, 4, 5])) # 5
