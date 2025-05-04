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

def characterReplacement(self, s: str, k: int) -> int:
  count = {}
  result = 0
  left = 0
  maxf = 0
  for right in range(len(s)):
    count[s[right]] = 1 + count.get(s[right], 0)
    maxf = max(maxf, count[s[right]])

    while (right - left + 1) - maxf > k:
      count[s[left]] -= 1
      left += 1
            
    result = max(result, right - left + 1)
  return result

if __name__ == "__main__":
  s = "XYYX"
  k = 2
  print(characterReplacement(s, k)) # Output: 4
  s = "AAABABB"
  k = 1
  print(characterReplacement(s, k)) # Output: 5