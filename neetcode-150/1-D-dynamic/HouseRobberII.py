# 213 - House Robber II
# Leetcode Link: https://leetcode.com/problems/house-robber-ii/

'''
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [3,4,3]
Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
'''

# Recursion
# Time Complexity: O(2^n)
# Space Complexity: O(n)
def rob3(nums):
  if len(nums) == 1:
      return nums[0]
  def dfs(i, flag):
    if i >= len(nums) or (flag and i == len(nums) - 1):
      return 0
    return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or i == 0))
  return max(dfs(0, True), dfs(1, False))



# Dynamic Programming (Bottom-Up)
# Time Complexity: O(n)
# Space Complexity: O(n)
def rob2(nums):
  if len(nums) == 1:
    return nums[0]
  return max(helper(nums[1:]), helper(nums[:-1]))

def helper(nums):
  if not nums:
    return 0
  if len(nums) == 1:
    return nums[0]

  dp = [0] * len(nums)
  dp[0] = nums[0]
  dp[1] = max(nums[0], nums[1])

  for i in range(2, len(nums)):
    dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

  return dp[-1]



# Dynamic Programming (Top-Down)
# Time Complexity: O(n)
# Space Complexity: O(n)
def rob1(nums):
  if len(nums) == 1:
    return nums[0]

  memo = [[-1] * 2 for _ in range(len(nums))]

  def dfs(i, flag):
    if i >= len(nums) or (flag and i == len(nums) - 1):
      return 0
    if memo[i][flag] != -1:
      return memo[i][flag]
    memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or (i == 0)))
    return memo[i][flag]
  return max(dfs(0, True), dfs(1, False))



# Dynamic Programming (Space-Optimized)
# Time Complexity: O(n)
# Space Complexity: O(1)
def rob(nums):
  return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

def helper(nums):
  rob1, rob2 = 0, 0

  for num in nums:
    newRob = max(rob1 + num, rob2)
    rob1 = rob2
    rob2 = newRob
  return rob2

if __name__ == "__main__":
  nums = [3, 4, 3]
  nums1 = [2, 9, 8, 3, 6]
  print("Test Case 1: ", nums)
  print("Expected Output: 4")
  print("Test Case 2: ", nums1)
  print("Expected Output: 15\n")
  
  print("Dynamic Programming (Space-Optimized) -> Test Case 1: ", rob(nums))
  print("Dynamic Programming (Space-Optimized) -> Test Case 2: ", rob(nums1), "\n")
  
  print("Dynamic Programming (Top-Down) -> Test Case 1: ", rob1(nums))
  print("Dynamic Programming (Top-Down) -> Test Case 2: ", rob1(nums1), "\n")
  
  print("Dynamic Programming (Bottom-Up) -> Test Case 1: ", rob2(nums))
  print("Dynamic Programming (Bottom-Up) -> Test Case 2: ", rob2(nums1), "\n")
  
  print("Recursion -> Test Case 1: ", rob3(nums))
  print("Recursion -> Test Case 2: ", rob3(nums1), "\n")