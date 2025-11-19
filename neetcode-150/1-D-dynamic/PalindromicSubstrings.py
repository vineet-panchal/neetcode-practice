# 

'''
Given a string s, return the number of substrings within s that are palindromes.
A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
'''

# Solutions To The Problem:

# Brute Force
# Time Complexity: O(n^3)
# Space Complexity: O(1)
def countSubstrings2(s):
  res = 0
  for i in range(len(s)):
    for j in range(i, len(s)):
      l, r = i, j
      while l < r and s[l] == s[r]:
        l += 1
        r -= 1
      res += (l >= r)
  return res



# Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def countSubstrings1(s):
  n, res = len(s), 0
  dp = [[False] * n for _ in range(n)]
  for i in range(n - 1, -1, -1):
    for j in range(i, n):
      if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        dp[i][j] = True
        res += 1
  return res



# Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def countSubstrings(s):
  res = 0
  for i in range(len(s)):
    # odd length
    l, r = i, i
    while l >= 0 and r < len(s) and s[l] == s[r]:
      res += 1
      l -= 1
      r += 1
    # even length
    l, r = i, i + 1
    while l >= 0 and r < len(s) and s[l] == s[r]:
      res += 1
      l -= 1
      r += 1
  return res

if __name__ == "__main__":
  s = "abc"
  s1 = "aaa"
  print("Test Case 1: ", s)
  print("Expected Output: 3")
  print("Test Case 2: ", s1)
  print("Expected Output: 6\n")
  
  print("Two Pointers -> Test Case 1: ", countSubstrings(s))
  print("Two Pointers -> Test Case 2: ", countSubstrings(s1), "\n")
  
  print("Dynamic Programming -> Test Case 1: ", countSubstrings1(s))
  print("Dynamic Programming -> Test Case 2: ", countSubstrings1(s1), "\n")
  
  print("Brute Force -> Test Case 1: ", countSubstrings2(s))
  print("Brute Force -> Test Case 2: ", countSubstrings2(s1), "\n")