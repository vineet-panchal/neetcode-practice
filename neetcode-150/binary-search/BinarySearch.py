# 704 - Binary Search
# Leetcode Link: https://leetcode.com/problems/binary-search/

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''

# Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
def binarySearch(nums, target):
  left = 0 # set left pointer for window
  right = len(nums) - 1 # set right pointer to the end of the window
  
  while left <= right: # while left and right don't go over each other
    mid = int(left + (right - left) / 2) 
    # calculate mid with right - left / 2 + left
    if target > nums[mid]: # if target is greater than element at mid
      left = mid + 1 # then target is on right of mid, move left to after mid
    elif target < nums[mid]: # if target is less than element at mid
      right = mid - 1 # then target is on the left of mid, move right to before mid
    else: # else target = element at mid
      return mid # return mid index
  return -1 # else return -1, if we could find it

if __name__ == "__main__":
  print(binarySearch([-1, 0, 2, 4, 6, 8], 4))