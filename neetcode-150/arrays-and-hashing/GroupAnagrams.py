# 49 - Group Anagrams
# Leetcode Link: https://leetcode.com/problems/group-anagrams/

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

'''
Initial Thoughts

Simplify the problem:
  - we aer given a list of strings, and we are to return a lists of lists, where each list is a group of strings, which are anagrams

Pattern Recognition: Straightforward/Optimal solution
  - we would have to find a way where we can get a frequency count of characters of each string, and match it, then just form a list
  - we obviously need a hashmap to count the frequency of characters for each string, but how would we do it, because there is more than one string
  - what if we group the strings in the hashmap as the values, already in a list, then the count would be the key
  - ok, so we would have to use a default dictionary and map each value as a list
  - we can then loop through the list and for each string, we create a list of 26 elements representing each character
  - then we loop through the string, and add 1 to the count at that letter, that would then be our key
  - we would append that string to that count, but here is the thing lists cannot be keys for a dictionary because they are mutable
  - so we can convert the count of letters into a tuple
  - at the end all of our groupings would be in values so we can just convert values to a list.
'''

from collections import defaultdict

# Hashmaps
# Time Complexity: O(m * n)
# Space Complexity: O(n)
def groupAnagrams(strs):
  res = defaultdict(list) # initialize the default dict
  for s in strs: # for each string in the list
    count = [0] * 26 # create a character count array, one for each letter
    for c in s: # for each character in a string
      count[ord(c) - ord('a')] += 1 # map each letter to its position in the alphabet
    res[tuple(count)].append(s) # use the count as a key, convert the list to a tuple, use it as a key to group anagrams together
  return list(res.values()) # return all grouped anagrams

if __name__ == "__main__":
  # Test cases
  print(groupAnagrams(["act","pots","tops","cat","stop","hat"])) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
  print(groupAnagrams(["x"])) # [["x"]]
  print(groupAnagrams([""])) # [[""]]