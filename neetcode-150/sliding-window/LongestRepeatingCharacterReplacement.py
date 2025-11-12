'''
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5
'''

def characterReplacement(s, k) -> int:
  count = {} # to track character frequencies in current window
  result = 0 # maximum valid window size found
  left = 0 # set left pointer to the stasrt of string
  maxf = 0 # maximum frequency of any character seen so far in the window
  for right in range(len(s)): # set right pointer to loop through the list
    count[s[right]] = 1 + count.get(s[right], 0)
    maxf = max(maxf, count[s[right]])
    # 1. Expand window: add character at 'right'
    # add the new character adn update maxf if this character becomes more frequent

    while (right - left + 1) - maxf > k: 
      count[s[left]] -= 1
      left += 1
    # 1. shrink window if invalid
    # if we need more than k replacements, shrink from the left to right
            
    result = max(result, right - left + 1)
    # 3. update result with current window size
  return result

if __name__ == "__main__":
  s = "XYYX"
  k = 2
  print(characterReplacement(s, k)) # Output: 4
  s = "AAABABB"
  k = 1
  print(characterReplacement(s, k)) # Output: 5