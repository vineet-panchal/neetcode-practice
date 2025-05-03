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

def isPalindrome(self, s: str) -> bool:
  strWithoutPunct = ""
  for char in s:
    if char.isalnum():
      strWithoutPunct += char.lower()
  return strWithoutPunct == strWithoutPunct[::-1]
# Time complexity: O(n)
# Space complexity: O(n)
# The time complexity is O(n) because we are iterating through the string once to create strWithoutPunct, and then we are checking if strWithoutPunct is equal to its reverse, which takes O(n) time.

def isPalindrome1(self, s: str) -> bool:
  left = 0
  right = len(s) - 1

  while left < right:
    while left < right and not self.alphaNum(s[left]):
      left += 1
    while right > left and not self.alphaNum(s[right]):
      right -= 1
    if s[left].lower() != s[right].lower():
      return False
    left += 1
    right -= 1
  return True

def alphaNum(self, c):
  return (ord('A') <= ord(c) <= ord('Z') or
          ord('a') <= ord(c) <= ord('z') or
          ord('0') <= ord(c) <= ord('9'))
# Time complexity: O(n)
# Space complexity: O(1)
# The time complexity is O(n) because we are iterating through the string once, and the space complexity is O(1) because we are using only a constant amount of extra space for the left and right pointers.

if __name__ == "__main__":
  s = "Was it a car or a cat I saw?"
  print(isPalindrome(s)) # Output: true
  print(isPalindrome1(s)) # Output: true
  s = "tab a cat"
  print(isPalindrome(s)) # Output: false
  print(isPalindrome1(s)) # Output: false