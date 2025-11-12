'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
Return the integer that represents the evaluation of the expression.
The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
'''

# Brute Force Approach
def evalRPN(tokens) -> int:
  while len(tokens) > 1:
    for i in range(len(tokens)):
      if tokens[i] in "+-*/":
        a = int(tokens[i-2])
        b = int(tokens[i-1])
        
        if tokens[i] == '+':
          result = a + b
        elif tokens[i] == '-':
          result = a - b
        elif tokens[i] == '*':
          result = a * b
        elif tokens[i] == '/':
            result = int(a / b)
        tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
        break
  return int(tokens[0])
# Time Complexity: O(n^2)
# Space Complexity: O(n)



# Doubly Linked List Approach
class DoublyLinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
def evalRPN1(tokens) -> int:
  head = DoublyLinkedList(tokens[0])
  curr = head

  for i in range(1, len(tokens)):
    curr.next = DoublyLinkedList(tokens[i], prev=curr)
    curr = curr.next

  while head is not None:
    if head.val in "+-*/":
      l = int(head.prev.prev.val)
      r = int(head.prev.val)
      if head.val == '+':
        res = l + r
      elif head.val == '-':
        res = l - r
      elif head.val == '*':
        res = l * r
      else:
        res = int(l / r)

      head.val = str(res)
      head.prev = head.prev.prev.prev
      if head.prev is not None:
        head.prev.next = head

    ans = int(head.val)
    head = head.next

  return ans
# Time Complexity: O(n)
# Space Complexity: O(n)



# Recursion Approach
def evalRPN2(tokens) -> int:
  def dfs():
    token = tokens.pop()
    if token not in "+-*/":
      return int(token)
            
    right = dfs()
    left = dfs()
            
    if token == '+':
      return left + right
    elif token == '-':
      return left - right
    elif token == '*':
      return left * right
    elif token == '/':
      return int(left / right)
        
  return dfs()
# Time Complexity: O(n)
# Space Complexity: O(n)



# Stack Approach
def evalRPN3(tokens) -> int:
  stack = [] # create a stack to track operations, store numbers in here
  for c in tokens: # for every character in tokens
    if c == "+": # if the character is +
      stack.append(stack.pop() + stack.pop()) 
      # add the sum of the two elements and add it to the stack
    elif c == "-": # if the character is -
      a, b = stack.pop(), stack.pop() # grab the elements that are being looked at
      stack.append(b - a) # subtract the numbers and add them to the stack
    elif c == "*": # if the character is *
      stack.append(stack.pop() * stack.pop()) 
      # multiply the two elements, and add it to the stack
    elif c == "/": # if the character is /
      a, b = stack.pop(), stack.pop() # grab the two elements being looked at
      stack.append(int(float(b) / a)) # divide the two elements and add them to the stack
    else: # else the character is a number
      stack.append(int(c)) # append the number to the stack
  return stack[0] # return the result. There should only be one element in the stack at the end
# Time Complexity: O(n)
# Space Complexity: O(n)


# Test Cases
if __name__ == "__main__":
  tokens = ["1","2","+","3","*","4","-"]
  print(evalRPN(tokens)) # Output: 5
  print(evalRPN1(tokens)) # Output: 5
  print(evalRPN2(tokens)) # Output: 5
  print(evalRPN3(tokens)) # Output: 5