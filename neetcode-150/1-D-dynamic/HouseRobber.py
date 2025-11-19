# 198 - House Robber
# Leetcode Link: https://leetcode.com/problems/house-robber/

'''
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.
You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [1,1,3,3]
Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
'''

# Dynamic Progamming (Space-Optimized)
# Time Complexity: O(n)
# Space Complexity: O(1)
def rob3(nums):
  rob1, rob2 = 0, 0

  for num in nums:
    temp = max(num + rob1, rob2)
    rob1 = rob2
    rob2 = temp
  return rob2



# Dynamic Programming (Bottom-Up)
# Time Complexity: O(n)
# Space Complexity: O(n)
def rob2(nums):
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
  memo = [-1] * len(nums)
  def dfs(i):
    if i >= len(nums):
      return 0
    if memo[i] != -1:
      return memo[i]
    memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
    return memo[i]
  return dfs(0)



# Recursion
# Time Complexity: O(2^n)
# Space Complexity: O(n)
def rob(nums):
  def dfs(i):
    if i >= len(nums):
      return 0
    return max(dfs(i + 1), nums[i] + dfs(i + 2))
  return dfs(0)

if __name__ == "__main__":
  nums = [1, 1, 3, 3]
  nums1 = [2, 9, 8, 3, 6]
  print("Test Case 1: ", nums)
  print("Expected Output: 4")
  print("Test Case 2: ", nums1)
  print("Expected Output: 16\n")
  
  print("Recursion -> Test Case 1: ", rob(nums))
  print("Recursion -> Test Case 2: ", rob(nums1), "\n")
  
  print("Dynamic Programming (Top-Down) -> Test Case 1: ", rob1(nums))
  print("Dynamic Programming (Top-Down) -> Test Case 2: ", rob1(nums1), "\n")
  
  print("Dynamic Programming (Bottom-Up) -> Test Case 1: ", rob2(nums))
  print("Dynamic Programming (Bottom-Up) -> Test Case 2: ", rob2(nums1), "\n")
  
  print("Dynamic Programming (Space-Optimized) -> Test Case 1: ", rob(nums))
  print("Dynamic Programming (Space-Optimized) -> Test Case 2: ", rob(nums1), "\n")