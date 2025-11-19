# 70 - Climbing Stairs
# Leetcode Link: https://leetcode.com/problems/climbing-stairs/

'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# Brute Force
# Time Complexity: O(n)
# Space Complexity: O(1)
def climbStairs(n: int) -> int:
  if n <= 3:
    return n
  n1, n2 = 2, 3

  for i in range(4, n + 1):
    temp = n1 + n2
    n1 = n2
    n2 = temp
    # n1, n2 = n2, n1 + n2
  return n2

if __name__ == "__main__":
  print("Test Case 1: 2")
  print("Expected Output: 2")
  print("Test Case 2: 3")
  print("Expected Output: 3\n")
  
  print("Brute Force -> Test Case 1: ", climbStairs(2))
  print("Brute Force -> Test Case 2: ", climbStairs(3))