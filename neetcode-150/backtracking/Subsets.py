'''
Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [7]
Output: [[],[7]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''

# Solutions To The Problem

# Iteration
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) extra space, O(2^n) for the output list
def subsets1(nums):
  res = [[]]
  for num in nums:
    res += [subset + [num] for subset in res]
  return res



# Backtracking
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n) extra space, O(2^n) for the output list
def subsets(nums):
  res = []
  subset = []

  def dfs(i):
    if i >= len(nums):
      res.append(subset.copy())
      return
    subset.append(nums[i])
    dfs(i + 1)
    subset.pop()
    dfs(i + 1)

  dfs(0)
  return res

if __name__ == "__main__":
  nums = [1, 2, 3]
  nums1 = [7]
  print("Test Case 1: nums = ", nums)
  print("Expected Output: ", [[], [1], [2], [3], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
  print("Test Case 2: nums = ", nums1)
  print("Expected Output: ", [[], [7]], "\n")
  
  print("Backtracking -> Test Case 1: ", subsets(nums))
  print("Backtracking -> Test Case 2: ", subsets(nums1), "\n")
  
  print("Iteration -> Test Case 1: ", subsets1(nums))
  print("Iteration -> Test Case 2: ", subsets1(nums1), "\n")