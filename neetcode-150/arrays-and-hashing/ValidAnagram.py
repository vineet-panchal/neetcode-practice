# 242 - Valid Anagram
# Leetcode Link: https://leetcode.com/problems/valid-anagram/

'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false
'''

'''
Initial Thougths

Simplify the problem:
  - we are given two strings, and we are to check if they are an anagram of eachother
  - an anagram of a string is a string the exact same characters but in a different order 

Pattern Recognition: Straightforward/Optimal solution
  - first of all a quick check would be to check the lengths of the two strings
  - if they are not the same, then they are obviously not an anagram
  - we have to get a count of each character in both strings, so we can have a hashmap for each string
  - we can then go over the count of each character in both hashmaps, and check if they are the same
  - if they are not the same return false, and return true at the end 
'''

# Solutions To The Problem:
from collections import Counter 
from collections import defaultdict

# Using Two Hashmaps
# Time complexity: O(n)
# Space complexity: O(n)
def validAnagram(s, t):
  if len(s) != len(t): 
    return False

  countS, countT = {}, {}
  for i in range(len(s)):
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)
        
  for c in countS:
    if countS[c] != countT.get(c, 0):
      return False
        
  return True



# Using a Default Dict
# Time Complexity: O(n)
# Space Complexity: O(n)
def validAnagram2(s, t):
  if len(s) != len(t):  
    return False
    
  countS, countT = defaultdict(int), defaultdict(int)
  for i in range(len(s)):
    countS[s[i]] += 1
    countT[t[i]] += 1
    
  for c in countS:
    if countS[c] != countT[c]:
      return False
  return True



# Using 1 Hashmap Only
# Time complexity: O(n)
# Space complexity: O(n)
def validAnagram3(s, t):
  if len(s) != len(t): 
    return False
  count = {}
  for i in range(len(s)):
    count[s[i]] = 1 + count.get(s[i], 0)
    count[t[i]] = count.get(t[i], 0) - 1
  for c in count:
    if count[c] != 0:
      return False        
  return True



# Using Counter
# Time complexity: O(n)
# Space complexity: O(n)
def validAnagram4(s, t):
  return Counter(s) == Counter(t)

if __name__ == "__main__":
  # Test cases
  print(validAnagram("racecar", "carrace")) # True
  print(validAnagram("jar", "jam")) # False
  print(validAnagram2("racecar", "carrace")) # True
  print(validAnagram2("jar", "jam")) # False
  print(validAnagram3("racecar", "carrace")) # True
  print(validAnagram3("jar", "jam")) # False