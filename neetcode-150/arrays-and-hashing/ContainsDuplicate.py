# 217 - Contains Duplicate
# Leetcode Link: https://leetcode.com/problems/contains-duplicate/

'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
'''

'''
Step 1: The input is a list of numbers, check if there is duplicate, if so return True, else return False
Step 2: We have to keep track of what we see in the list. A hashmap could be useful here
Step 3: Loop through the list and put elements in the hashmap. If a element is already in the hashmap return true. If you loop through all the elements then return false.
'''

'''
Initial Thougths

Simplify the problem:
  - given a list, we return true if the list has a duplicate element

Pattern Recognition: Straightforward/Optimal solution
  - we obviously need a way to track what we've already seen before while looping through the list
  - we can initialize a set, then when we loop through the list, we check if the element is already in the set
  - if it is in the set, then we found a duplicate, return true, else add it to the set
'''

# Solutions To The Problem:

# Sets
# Time complexity: O(n)
# Space complexity: O(n)
def containsDuplicate1(nums):
  seen = set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False



# Compare Length of List and its Set
# Time complexity: O(n)
# Space complexity: O(n)
def containsDuplicate2(nums):
  return len(nums) != len(set(nums))


# Hashmaps
# Time complexity: O(n)
# Space complexity: O(n)
def containsDuplicate3(nums):
  seen = {}
  for num in nums:
    if num in seen:
      return True
    seen[num] = 1
  return False

if __name__ == "__main__":
  # Test cases
  print(containsDuplicate1([1, 2, 3, 3])) # True
  print(containsDuplicate1([1, 2, 3, 4])) # False
  print(containsDuplicate2([1, 2, 3, 3])) # True
  print(containsDuplicate2([1, 2, 3, 4])) # False
  print(containsDuplicate3([1, 2, 3, 3])) # True
  print(containsDuplicate3([1, 2, 3, 4])) # False