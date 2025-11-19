# 746 - Min Cost Climbing Stairs
# Leetcode Link: https://leetcode.com/problems/min-cost-climbing-stairs/

'''
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.
You may choose to start at the index 0 or the index 1 floor.
Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

Example 1:
Input: cost = [1,2,3]
Output: 2
Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two steps to reach the top. The total cost is 2.

Example 2:
Input: cost = [1,2,1,2,1,1,1]
Output: 4
Explanation: Start at index = 0.
Pay the cost of cost[0] = 1 and take two steps to reach index = 2.
Pay the cost of cost[2] = 1 and take two steps to reach index = 4.
Pay the cost of cost[4] = 1 and take two steps to reach index = 6.
Pay the cost of cost[6] = 1 and take one step to reach the top.
The total cost is 4.

Constraints:
2 <= cost.length <= 100
0 <= cost[i] <= 100
'''

# Solutions To The Problem:

# Dynamic Programming (Space-Optimized)
# Time Complexity: O(n)
# Space Complexity: O(1)
def minCostClimbingStairs3(cost):
  for i in range(len(cost) - 3, -1, -1):
    cost[i] += min(cost[i + 1], cost[i + 2])
  return min(cost[0], cost[1])



# Dynamic Programming (Bottom-Up)
# Time Complexity: O(n)
# Space Complexity: O(n)
def minCostClimbingStairs2(cost):
  n = len(cost)
  dp = [0] * (n + 1)
  for i in range(2, n + 1):
    dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
  return dp[n]



# Dynamic Programming (Top-Down)
# Time Complexity: O(n)
# Space Complexity: O(n)
def minCostClimbingStairs1(cost):
  memo = [-1] * len(cost)
  def dfs(i):
    if i >= len(cost):
      return 0
    if memo[i] != -1:
      return memo[i]
    memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
    return memo[i]
  return min(dfs(0), dfs(1))



# Recursion
# Time Complexity: O(2^n)
# Space Complexity: O(n)
def minCostClimbingStairs(cost):
  def dfs(i):
    if i >= len(cost):
      return 0
    return cost[i] + min(dfs(i + 1), dfs(i + 2))

  return min(dfs(0), dfs(1))

if __name__ == "__main__":
  cost = [1, 2, 1]
  cost1 = [1, 2, 1, 2, 1, 1, 1]
  print("Test Case 1: ", cost)
  print("Expected Output: 2")
  print("Test Case 2: ", cost1)
  print("Expected Output: 4\n")
  
  print("Recursion -> Test Case 1: ", minCostClimbingStairs(cost))
  print("Recursion -> Test Case 2: ", minCostClimbingStairs(cost1), "\n")
  
  print("Dynamic Programming (Top-Down) -> Test Case 1: ", minCostClimbingStairs(cost))
  print("Dynamic Programming (Top-Down) -> Test Case 2: ", minCostClimbingStairs(cost1), "\n")
  
  print("Dynamic Programming (Bottom-Up) -> Test Case 1: ", minCostClimbingStairs(cost))
  print("Dynamic Programming (Bottom-Up) -> Test Case 2: ", minCostClimbingStairs(cost1), "\n")
  
  print("Dynamic Progamming (Space-Optimized) -> Test Case 1: ", minCostClimbingStairs(cost))
  print("Dynamic Progamming (Space-Optimized) -> Test Case 2: ", minCostClimbingStairs(cost), "\n")