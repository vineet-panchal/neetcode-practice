'''
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
Both strings only contain lowercase letters.

Example 1:
Input: s1 = "abc", s2 = "lecabee"
Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:
Input: s1 = "abc", s2 = "lecaabee"
Output: false
'''

def checkInclusion(self, s1: str, s2: str) -> bool:
  s1 = sorted(s1)

  for i in range(len(s2)):
    for j in range(i, len(s2)):
      subStr = s2[i : j + 1]
      subStr = sorted(subStr)
      if subStr == s1:
        return True
  return False
# Time complexity: O(N^2 * M log M)
# Space complexity: O(M)
# The above code is a brute force approach to check if s2 contains a permutation of s1.
# It uses a nested loop to generate all substrings of s2 and checks if any of them is a permutation of s1.
# The first function sorts both s1 and the substring of s2 and compares them.
# The time complexity is O(N^2 * M log M) because of the nested loops and sorting, and the space complexity is O(M) for the sorted substring.
# The brute force approach is inefficient for larger strings as it has a time complexity of O(N^2 * M log M).
# The above code is a brute force approach to check if s2 contains a permutation of s1.
# It uses a nested loop to generate all substrings of s2 and checks if any of them is a permutation of s1.

def checkInclusion1(s1, s2) -> bool:
  count1 = {} # to track what we have seen in string 1
  for c in s1: # for every character in string 1
    count1[c] = 1 + count1.get(c, 0) # add 1 if we have seen it, else set it to 0
        
  need = len(count1) # get the length of count 1
  for i in range(len(s2)): # let i be the left pointer, to loop through string 2
    count2, cur = {}, 0 # count2 to track what is seen in string 2, 
    for j in range(i, len(s2)): # let j be the right pointer, to loop through string 1, starting from i
      count2[s2[j]] = 1 + count2.get(s2[j], 0) # counts frequency of characters for string 2
      if count1.get(s2[j], 0) < count2[s2[j]]: 
      # if we have more of a character than string 1 has, this window cannot be a permutation
      # break and try the next starting position
        break
      if count1.get(s2[j], 0) == count2[s2[j]]:
      # when a character's frequency matches exactly, increment cur
        cur += 1
      if cur == need:
      # when cur == need, we've matched all unique characters with correct frequencies
        return True
  return False
# Time complexity: O(N^2)
# Space complexity: O(N)
# The above code is a brute force approach to check if s2 contains a permutation of s1.
# It uses a nested loop to generate all substrings of s2 and checks if any of them is a permutation of s1.
# The first function sorts both s1 and the substring of s2 and compares them.
# The second function uses a dictionary to count the frequency of characters in s1 and s2.
# It checks if the frequency of characters in the substring of s2 matches that of s1.
# The time complexity is O(N^2) because of the nested loops, and the space complexity is O(N) for the count dictionaries.
# The brute force approach is inefficient for larger strings as it has a time complexity of O(N^2).
# The above code is a brute force approach to check if s2 contains a permutation of s1.


def checkInclusion2(self, s1: str, s2: str) -> bool:
  if len(s1) > len(s2):
    return False
        
  s1Count, s2Count = [0] * 26, [0] * 26
  for i in range(len(s1)):
    s1Count[ord(s1[i]) - ord('a')] += 1
    s2Count[ord(s2[i]) - ord('a')] += 1
        
  matches = 0
  for i in range(26):
    matches += (1 if s1Count[i] == s2Count[i] else 0)
        
  l = 0
  for r in range(len(s1), len(s2)):
    if matches == 26:
      return True
            
    index = ord(s2[r]) - ord('a')
    s2Count[index] += 1
    if s1Count[index] == s2Count[index]:
      matches += 1
    elif s1Count[index] + 1 == s2Count[index]:
      matches -= 1

    index = ord(s2[l]) - ord('a')
    s2Count[index] -= 1
    if s1Count[index] == s2Count[index]:
      matches += 1
    elif s1Count[index] - 1 == s2Count[index]:
      matches -= 1
    l += 1
  return matches == 26
# Time complexity: O(N)
# Space complexity: O(1) because the size of the count array is constant (26 for lowercase letters)
# The above code is a sliding window approach to check if s2 contains a permutation of s1.
# It uses two arrays of size 26 to count the frequency of characters in s1 and s2.
# The matches variable keeps track of how many characters have the same frequency in both arrays.
# The window slides through s2, updating the counts and checking if all characters match.
# The final check is if matches equals 26, which means all characters match.
# The time complexity is O(N) because we iterate through s2 once, and the space complexity is O(1) because the size of the count arrays is constant.
# The sliding window approach is efficient for this problem as it reduces the time complexity from O(N^2) to O(N).

if __name__ == "__main__":
  s1 = "abc"
  s2 = "lecabee"
  print(checkInclusion(s1, s2)) # Output: True
  s1 = "abc"
  s2 = "lecaabee"
  print(checkInclusion(s1, s2)) # Output: False
  s1 = "abc"
  s2 = "lecababc"
  print(checkInclusion(s1, s2)) # Output: True
  s1 = "abc"
  s2 = "lecaababc"
  print(checkInclusion(s1, s2)) # Output: False
  
  s1 = "abc"
  s2 = "lecabee"
  print(checkInclusion1(s1, s2)) # Output: True
  s1 = "abc"
  s2 = "lecaabee"
  print(checkInclusion1(s1, s2)) # Output: False
  s1 = "abc"
  s2 = "lecababc"
  print(checkInclusion1(s1, s2)) # Output: True
  s1 = "abc"
  s2 = "lecaababc"
  print(checkInclusion1(s1, s2)) # Output: False

  s1 = "abc"
  s2 = "lecabee"
  print(checkInclusion2(s1, s2)) # Output: True
  s1 = "abc"
  s2 = "lecaabee"
  print(checkInclusion2(s1, s2)) # Output: False
  s1 = "abc"
  s2 = "lecababc"
  print(checkInclusion2(s1, s2)) # Output: True
  s1 = "abc"
  s2 = "lecaababc"
  print(checkInclusion2(s1, s2)) # Output: False