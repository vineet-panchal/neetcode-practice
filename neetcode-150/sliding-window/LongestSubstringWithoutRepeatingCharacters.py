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

def lengthOfLongestSubstring(s) -> int:
  charSet = set() # initialize a charset, to keep track of chars that we haven't seen
  left = 0 # set left pointer to the start of the list
  result = 0 # set the result to 0, length of the longest substring

  for right in range(len(s)): # set right pointer to go through the list
    while s[right] in charSet: # while right element is in the character set
      charSet.remove(s[left]) # remove left element from the character set
      left += 1 # increment the left pointer
    charSet.add(s[right]) # if right element is not in the character set, add the right element
    result = max(result, right - left + 1) 
    # get the max length by comparing the previous length with the right pointer - left pointer + 1
  
  return result # return the max length

if __name__ == "__main__":
  s = "zxyzxyz"
  print(lengthOfLongestSubstring(s))
  s = "xxxx"
  print(lengthOfLongestSubstring(s))