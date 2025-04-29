'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]
'''

from collections import defaultdict

# solution 1
def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
    return list(anagrams.values())
# Time complexity: O(n * k log k), where n is the number of strings and k is the maximum length of a string
# Space complexity: O(n * k), where n is the number of strings and k is the maximum length of a string

# solution 2
def groupAnagrams2(strs):
  res = defaultdict(list)
  for s in strs:
    count = [0] * 26
    for c in s:
      count[ord(c) - ord('a')] += 1
    res[tuple(count)].append(s)
  return list(res.values())

if __name__ == "__main__":
  # Test cases
  print(groupAnagrams(["act","pots","tops","cat","stop","hat"])) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
  print(groupAnagrams(["x"])) # [["x"]]
  print(groupAnagrams([""])) # [[""]]
  print(groupAnagrams2(["act","pots","tops","cat","stop","hat"])) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
  print(groupAnagrams2(["x"])) # [["x"]]
  print(groupAnagrams2([""])) # [[""]]