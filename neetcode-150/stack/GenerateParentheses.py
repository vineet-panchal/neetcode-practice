'''
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:
Input: n = 1
Output: ["()"]

Example 2:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.
'''

# Brute Force Approach
def generateParenthesis(n):
  res = []

  def valid(s: str):
    open = 0
    for c in s:
      open += 1 if c == '(' else -1
      if open < 0:
        return False
    return not open

  def dfs(s: str):
    if n * 2 == len(s):
      if valid(s):
        res.append(s)
      return
            
    dfs(s + '(')
    dfs(s + ')')
  dfs("")
  return res
# Time Complexity: O(2^(2n)) because we are generating all possible combinations of parentheses
# Space Complexity: O(n) for the recursion stack



# Backtracking Approach
def generateParenthesis1(n):
  stack = []
  res = []

  def backtrack(openN, closedN):
    if openN == closedN == n:
      res.append("".join(stack))
      return

    if openN < n:
      stack.append("(")
      backtrack(openN + 1, closedN)
      stack.pop()
    if closedN < openN:
      stack.append(")")
      backtrack(openN, closedN + 1)
      stack.pop()

  backtrack(0, 0)
  return res
# Time Complexity: O(4^n/sqrt(n)) because the number of valid parentheses combinations is given by the Catalan number
# Space Complexity: O(n) for the recursion stack



# Dynamic Programming Approach
def generateParenthesis2(n):
  res = [[] for _ in range(n+1)]
  res[0] = [""]
        
  for k in range(n + 1):
    for i in range(k):
      for left in res[i]:
        for right in res[k-i-1]:
          res[k].append("(" + left + ")" + right)
        
  return res[-1]
# Time Complexity: O(4^n/sqrt(n)) because the number of valid parentheses combinations is given by the Catalan number
# Space Complexity: O(n) for the recursion stack

# Test Cases
if __name__ == "__main__":
  n = 3
  print(generateParenthesis(n)) # ["((()))","(()())","(())()","()(())","()()()"]
  print(generateParenthesis1(n)) # ["((()))","(()())","(())()","()(())","()()()"]
  print(generateParenthesis2(n)) # ["((()))","(()())","(())()","()(())","()()()"]
  n = 1
  print(generateParenthesis(n)) # ["()"]
  print(generateParenthesis1(n)) # ["()"]
  print(generateParenthesis2(n)) # ["()"]
