'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
'''

# solution 1
def containsDuplicate1(nums):
  seen = set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False
# Time complexity: O(n)
# Space complexity: O(n)

# solution 2
def containsDuplicate2(nums):
  return len(nums) != len(set(nums))
# Time complexity: O(n)
# Space complexity: O(n)

# solution 3
def containsDuplicate3(nums):
  nums.sort()
  for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
      return True
  return False

# Time complexity: O(n log n)
# Space complexity: O(1)

# solution 4
def containsDuplicate4(nums):
  seen = {}
  for num in nums:
    if num in seen:
      return True
    seen[num] = 1
  return False
# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == "__main__":
  # Test cases
  print(containsDuplicate1([1, 2, 3, 3])) # True
  print(containsDuplicate1([1, 2, 3, 4])) # False
  print(containsDuplicate2([1, 2, 3, 3])) # True
  print(containsDuplicate2([1, 2, 3, 4])) # False
  print(containsDuplicate3([1, 2, 3, 3])) # True
  print(containsDuplicate3([1, 2, 3, 4])) # False
  print(containsDuplicate4([1, 2, 3, 3])) # True
  print(containsDuplicate4([1, 2, 3, 4])) # False