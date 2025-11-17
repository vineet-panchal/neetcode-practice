# 215 - Kth Largest Element in an Array
# Leetcode Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

'''
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

# Solutions To The Problem:
import heapq

# Quick Select
# Time Complexity: O(n)
# Space Complexity: O(n)
def findKthLargest2(nums, k):
  k = len(nums) - k
  def quickSelect(l, r):
    pivot, p = nums[r], l
    for i in range(l, r):
      if nums[i] <= pivot:
        nums[p], nums[i] = nums[i], nums[p]
        p += 1
    nums[p], nums[r] = nums[r], nums[p]

    if p > k:
      return quickSelect(l, p - 1)
    elif p < k:
      return quickSelect(p + 1, r)
    else:
      return nums[p]
  return quickSelect(0, len(nums) - 1)



# Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def findKthLargest1(nums, k):
  nums.sort()
  return nums[len(nums) - k]



# Min-Heap
# Time Complexity: O(n log k)
# Space Complexity: O(k)
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

if __name__ == "__main__":
  nums = [2, 3, 1, 5, 4]
  k = 2
  nums1 = [2, 3, 1, 1, 5, 5, 4]
  k1 = 3
  print("Test Case 1: nums = ", nums, " k = ", k)
  print("Expected Output: ", 4)
  print("Test Case 2: nums = ", nums1, " k = ", k1)
  print("Expected Output: ", 4, "\n")
  
  print("Min-Heap -> Test Case 1: ", findKthLargest(nums, k))
  print("Min-Heap -> Test Case 2: ", findKthLargest(nums1, k1), "\n")
  
  print("Sorting -> Test Case 1: ", findKthLargest1(nums, k))
  print("Sorting -> Test Case 2: ", findKthLargest1(nums1, k1), "\n")
  
  print("Quick Select -> Test Case 1: ", findKthLargest2(nums, k))
  print("Quick Select -> Test Case 2: ", findKthLargest2(nums1, k1), "\n")