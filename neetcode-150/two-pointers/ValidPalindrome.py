# 125 - Valid Palindrome
# Leetcode Link: https://leetcode.com/problems/valid-palindrome/

'''
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
'''

# Solutions To The Problem:

# Check Reverse
# Time complexity: O(n)
# Space complexity: O(n)
def isPalindrome(s) -> bool:
  strWithoutPunct = ""
  for char in s:
    if char.isalnum():
      strWithoutPunct += char.lower()
  return strWithoutPunct == strWithoutPunct[::-1]



# Making Alphanumeric Function
# Time Complexity: O(n)
# Space Complexity: O(1)
def alphaNum(c):
  return (ord('A') <= ord(c) <= ord('Z') or
          ord('a') <= ord(c) <= ord('z') or
          ord('0') <= ord(c) <= ord('9'))

def isPalindrome1(s) -> bool:
  left = 0
  right = len(s) - 1

  while left < right:
    while left < right and not alphaNum(s[left]):
      left += 1
    while right > left and not alphaNum(s[right]):
      right -= 1
    if s[left].lower() != s[right].lower():
      return False
    left += 1
    right -= 1
  return True



# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1) 
def isPalindrome2(s) -> bool:
  left = 0 # set left pointer to the index of start of the list
  right = len(s) - 1 # set right pointer to the index of the end of the list
  
  while left < right: 
  # while left pointer is less then the right pointer (they should never be the same)
    while left < right and not s[left].isalnum(): 
    # check if left is less than right, and the left element is not an alphanumeric
      left += 1 # then increase left's index
    while right > left and not s[right].isalnum(): 
    # check if right is greater than left, and the right element is not an alphanumeric
      right -= 1 # then decrease right's index
    if s[left].lower() != s[right].lower():
    # first make both left and right element equal, by making them both lowercase, then compare if they are the same or not
      return False # if they are not the same, we stop, and return false
    # else if they are the same, then:
    left += 1 # increment left pointer
    right -= 1 # decrement right pointer
  return True # we compared each two opposing elements, and they all pass, so return true

if __name__ == "__main__":
  s = "Was it a car or a cat I saw?"
  print(isPalindrome(s)) # Output: true
  print(isPalindrome1(s)) # Output: true
  print(isPalindrome2(s)) # true
  s = "tab a cat"
  print(isPalindrome(s)) # Output: false
  print(isPalindrome1(s)) # Output: false
  print(isPalindrome2(s)) # false