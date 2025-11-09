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
Step 1: Given two strings, check if they contain the same characters as another string, and return True, else return False
Step 2: We need to keep track of what we saw in each string, so a hashmap would be useful
Step 3: Use two different hashmaps to track the count of each character for each string, then we compare the two hashmaps.
'''

from collections import Counter 
from collections import defaultdict

# solution 1
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
# Time complexity: O(n)
# Space complexity: O(n)

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
# Time Complexity: O(n)
# Space Complexity: O(n)


# solution 2
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
# Time complexity: O(n)
# Space complexity: O(n)

# solution 3
def validAnagram4(s, t):
  return Counter(s) == Counter(t)
# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == "__main__":
  # Test cases
  print(validAnagram("racecar", "carrace")) # True
  print(validAnagram("jar", "jam")) # False
  print(validAnagram2("racecar", "carrace")) # True
  print(validAnagram2("jar", "jam")) # False
  print(validAnagram3("racecar", "carrace")) # True
  print(validAnagram3("jar", "jam")) # False