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
  numSet = set(nums) # cast arr as a set, to remove duplicate elements
  maxLength = 0 # set the maxlength to 0

  for n in nums: # loop through list
    if (n - 1) not in numSet: # if there isn't a previous consecutive num in the rest of the list, then
      currLength = 0 # set the current length to 0
      while (n + currLength) in numSet: # if n + current length is in the set
        currLength += 1 # increment the current length
      maxLength = max(currLength, maxLength) # get the max length, between current and max length
  return maxLength # return the max length

# Time complexity: O(n)
# Space complexity: O(n)
if __name__ == "__main__":
  # Test cases
  print(longestConsecutive([2, 20, 4, 10, 3, 4, 5])) # 4
  print(longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1])) # 7
  print(longestConsecutive([1, 2, 3, 4, 5])) # 5
