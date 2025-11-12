'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:
Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
'''

# Stack Approach
def isValid1(s: str) -> bool:
  stack = [] # 
  closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
  # maps each closing bracket to its corresponding opening bracket

  for c in s: # loop through the string using c
    if c in closeToOpen: # if it is a closing bracket
      if stack and stack[-1] == closeToOpen[c]: # check if the stack has an opening bracket on top
        stack.pop() # if yes, pop it off (we found a valid pair)
      else: # else no we did not find a opening bracket
        return False
    else: # if it is an opening bracket
      stack.append(c) # push it onto the stack (waiting for its closing bracket)
        
  return True if not stack else False # return true only if the stack is empty (all brackets were matched)
  # Time complexity: O(n)
  # Space complexity: O(n)



# Brute Force Approach
def isValid2(s: str) -> bool:
  while '()' in s or '{}' in s or '[]' in s:
    s = s.replace('()', '')
    s = s.replace('{}', '')
    s = s.replace('[]', '')
  return s == ''
# Time complexity: O(n^2)
# Space complexity: O(1)

if __name__ == "__main__":
  # Test cases
  print(isValid1("[]")) # True
  print(isValid1("([{}])")) # True
  print(isValid1("[(])")) # False
  
  print(isValid2("[]")) # True
  print(isValid2("([{}])")) # True
  print(isValid2("[(])")) # False