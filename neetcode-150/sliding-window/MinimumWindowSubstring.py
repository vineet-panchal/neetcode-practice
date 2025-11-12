'''
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
You may assume that the correct output is always unique.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3:
Input: s = "x", t = "xy"
Output: ""
'''

from collections import Counter

def minWindow(s: str, t: str) -> str:
  tCount = Counter(t) # count of each character needed from string t
  sCount = Counter() # count of characters in current window
  l = 0 # set left pointer of window
  minLength = float("inf") # track shortest valid window
  result = "" # store the resulting substring
  for r in range(len(s)): # set right pointer of window, to loop through string s
    sCount[s[r]] += 1 # add each character to the window by incrementing count in sCount
    while all(sCount[c] >= tCount[c] for c in tCount):
    # the window is valid when it contains all characters from t with sufficient counts
    # all(sCount[c] >= tCount[c] for c in tCount) checks if every character in string t
    # appears in the window at least as many times as needed
      if (r - l + 1) < minLength: # if current window is smaller than previous minimum, update the result
        minLength = r - l + 1
        result = s[l:r + 1]
      sCount[s[l]] -= 1
      if sCount[s[l]] == 0: # remove the left most character from the window
        del sCount[s[l]]
      l += 1 # move left pointer to right to try finding a smaller valid window
  return result
# Time Complexity: O(n + m)

def minWindow1(self, s: str, t: str) -> str:
  if t == "":
    return ""

  countT = {}
  for c in t:
    countT[c] = 1 + countT.get(c, 0)

  res, resLen = [-1, -1], float("infinity")
  for i in range(len(s)):
    countS = {}
    for j in range(i, len(s)):
      countS[s[j]] = 1 + countS.get(s[j], 0)

      flag = True
      for c in countT:
        if countT[c] > countS.get(c, 0):
          flag = False
          break
                
        if flag and (j - i + 1) < resLen:
          resLen = j - i + 1
          res = [i, j]

  l, r = res
  return s[l : r + 1] if resLen != float("infinity") else ""
  # Time complexity: O(n^2)
  # Space complexity: O(n)

def minWindow2(self, s: str, t: str) -> str:
  if t == "":
    return ""

  countT, window = {}, {}
  for c in t:
    countT[c] = 1 + countT.get(c, 0)

  have, need = 0, len(countT)
  res, resLen = [-1, -1], float("infinity")
  l = 0
  for r in range(len(s)):
    c = s[r]
    window[c] = 1 + window.get(c, 0)

    if c in countT and window[c] == countT[c]:
      have += 1

    while have == need:
      if (r - l + 1) < resLen:
        res = [l, r]
        resLen = r - l + 1
                    
      window[s[l]] -= 1
      if s[l] in countT and window[s[l]] < countT[s[l]]:
        have -= 1
        l += 1
  l, r = res
  return s[l : r + 1] if resLen != float("infinity") else ""
  # Time complexity: O(n)
  # Space complexity: O(n)

if __name__ == "__main__":
  # Test cases
  print(minWindow("ADOBECODEBANC", "ABC")) # "BANC"
  print(minWindow("a", "a")) # "a"
  print(minWindow("a", "aa")) # ""
  print(minWindow("aa", "aa")) # "aa"
  print(minWindow("a", "")) # ""
  print(minWindow("", "a")) # ""
  print(minWindow("", "")) # ""
  
  print(minWindow1("ADOBECODEBANC", "ABC")) # "BANC"
  print(minWindow1("a", "a")) # "a"
  print(minWindow1("a", "aa")) # ""
  print(minWindow1("aa", "aa")) # "aa"
  print(minWindow1("a", "")) # ""
  print(minWindow1("", "a")) # ""
  print(minWindow1("", "")) # ""
  
  print(minWindow2("ADOBECODEBANC", "ABC")) # "BANC"
  print(minWindow2("a", "a")) # "a"
  print(minWindow2("a", "aa")) # ""
  print(minWindow2("aa", "aa")) # "aa"
  print(minWindow2("a", "")) # ""
  print(minWindow2("", "a")) # ""
  print(minWindow2("", "")) # ""
