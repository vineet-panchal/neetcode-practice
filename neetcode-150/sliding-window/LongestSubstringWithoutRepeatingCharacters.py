'''
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1
'''

def lengthOfLongestSubstring(self, s: str) -> int:
  charSet = set()
  left = 0
  result = 0

  for right in range(len(s)):
    while s[right] in charSet:
      charSet.remove(s[left])
      left += 1
    charSet.add(s[right])
    result = max(result, right - left + 1)
  
  return result

if __name__ == "__main__":
  s = "zxyzxyz"
  print(lengthOfLongestSubstring(s))
  s = "xxxx"
  print(lengthOfLongestSubstring(s))