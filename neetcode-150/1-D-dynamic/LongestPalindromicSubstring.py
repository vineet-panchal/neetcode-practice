# 5 - Longest Palindromic Substring
# Leetcode Link: https://leetcode.com/problems/longest-palindromic-substring/

'''
Given a string s, return the longest substring of s that is a palindrome.
A palindrome is a string that reads the same forward and backward.
If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:
Input: s = "ababd"
Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:
Input: s = "abbc"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s contains only digits and English letters.
'''

# Solutions To The Problem:

# Brute Force
# Time Complexity: O(n^3)
# Space Complexity: O(n)
def longestPalindrome2(s):
  res, resLen = "", 0
  for i in range(len(s)):
    for j in range(i, len(s)):
      l, r = i, j
      while l < r and s[l] == s[r]:
        l += 1
        r -= 1
      if l >= r and resLen < (j - i + 1):
        res = s[i : j + 1]
        resLen = j - i + 1
  return res



# Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1) for extra space, O(n) for the output string
def longestPalindrome1(s):
  resIdx = 0
  resLen = 0
  for i in range(len(s)):
    # odd length
    l, r = i, i
    while l >= 0 and r < len(s) and s[l] == s[r]:
      if (r - l + 1) > resLen:
        resIdx = l
        resLen = r - l + 1
      l -= 1
      r += 1
    # even length
    l, r = i, i + 1
    while l >= 0 and r < len(s) and s[l] == s[r]:
      if (r - l + 1) > resLen:
        resIdx = l
        resLen = r - l + 1
      l -= 1
      r += 1
  return s[resIdx : resIdx + resLen]



# Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def longestPalindrome(s):
  resIdx, resLen = 0, 0
  n = len(s)
  dp = [[False] * n for _ in range(n)]
  for i in range(n - 1, -1, -1):
    for j in range(i, n):
      if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        dp[i][j] = True
        if resLen < (j - i + 1):
          resIdx = i
          resLen = j - i + 1
  return s[resIdx : resIdx + resLen]

if __name__ == "__main__":
  s = "ababd"
  s1 = "abbc"
  print("Test Case 1: ", s)
  print("Expected Output: bab")
  print("Test Case 2: ", s1)
  print("Expected Output: bb\n")
  
  print("Dynamic Programming -> Test Case 1: ", longestPalindrome(s))
  print("Dynamic Programming -> Test Case 2: ", longestPalindrome(s1), "\n")
  
  print("Two Pointers -> Test Case 1: ", longestPalindrome1(s))
  print("Two Pointers -> Test Case 2: ", longestPalindrome1(s1), "\n")
  
  print("Brute Force -> Test Case 1: ", longestPalindrome2(s))
  print("Brute Force -> Test Case 2: ", longestPalindrome2(s1), "\n")