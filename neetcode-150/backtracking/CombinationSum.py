# 39 - Combination Sum
# Leetcode Link: https://leetcode.com/problems/combination-sum/

'''
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:
Input: 
nums = [2,5,6,9] 
target = 9
Output: [[2,2,5],[9]]
Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:
Input: 
nums = [3,4,5]
target = 16
Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:
Input: 
nums = [3]
target = 5
Output: []

Constraints:
All elements of nums are distinct.
1 <= nums.length <= 20
2 <= nums[i] <= 30
2 <= target <= 30
'''

# Solutions To The Problem:

# Backtracking
# Time Complexity: O(2^t/m)
# Space Complexity: O(t/m)
def combinationSum(nums, target):
  res = []
  def dfs(i, cur, total):
    if total == target:
      res.append(cur.copy())
      return
    if i >= len(nums) or total > target:
      return
    cur.append(nums[i])
    dfs(i, cur, total + nums[i])
    cur.pop()
    dfs(i + 1, cur, total)
  dfs(0, [], 0)
  return res

if __name__ == "__main__":
  nums = [2, 5, 6, 9]
  target = 9
  nums1 = [3, 4, 5]
  target1 = 16
  nums2 = [3]
  target2 = 5
  print("Test Case 1: nums = ", nums, " target = ", target)
  print("Expected Output: ", [[2, 2, 5], [9]])
  print("Test Case 2: nums = ", nums1, " target = ", target1) 
  print("Expected Output: ", [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]])
  print("Test Case 3: nums = ", nums2, " target = ", target2)
  print("Expected Output: ", [], "\n")
  
  print("Backtracking -> Test Case 1: ", combinationSum(nums, target))
  print("Backtracking -> Test Case 2: ", combinationSum(nums1, target1))
  print("Backtracking -> Test Case 3: ", combinationSum(nums2, target2))