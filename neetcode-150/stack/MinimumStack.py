'''
Design a stack class that supports the push, pop, top, and getMin operations.
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Example 1:
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null,null,null,null,0,null,2,1]
Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
'''

# Brute Force Approach
class MinStack:
  def __init__(self):
    self.stack = []

  def push(self, val: int) -> None:
    self.stack.append(val)

  def pop(self) -> None:
    self.stack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    tmp = []
    mini = self.stack[-1]

    while len(self.stack):
      mini = min(mini, self.stack[-1])
      tmp.append(self.stack.pop())
          
    while len(tmp):
      self.stack.append(tmp.pop())
          
    return mini



# Two Stacks Approach
class MinStack1:
  def __init__(self):
    self.stack = []
    self.minStack1 = []

  def push1(self, val: int) -> None:
    self.stack.append(val)
    val = min(val, self.minStack1[-1] if self.minStack1 else val)
    self.minStack1.append(val)

  def pop(self) -> None:
    self.stack.pop()
    self.minStack1.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minStack1[-1]
# The time complexity of all the operations is O(1) in this approach.
# The space complexity is O(n) in this approach.



# One Stack Approach
class MinStack2:
  def __init__(self):
    self.min = float('inf')
    self.stack = []

  def push(self, val: int) -> None:
    if not self.stack:
      self.stack.append(0)
      self.min = val
    else:
      self.stack.append(val - self.min)
      if val < self.min:
        self.min = val

  def pop(self) -> None:
    if not self.stack:
      return
        
    pop = self.stack.pop()
        
    if pop < 0:
      self.min = self.min - pop

  def top(self) -> int:
    top = self.stack[-1]
    if top > 0:
      return top + self.min
    else:
      return self.min

  def getMin(self) -> int:
    return self.min
# The time complexity of all the operations is O(1) in this approach.
# The space complexity is O(n) in this approach.

# Test the code
if __name__ == "__main__":
  minStack = MinStack()
  minStack.push(1)
  minStack.push(2)
  minStack.push(0)
  print(minStack.getMin()) # return 0
  minStack.pop()
  print(minStack.top())    # return 2
  print(minStack.getMin()) # return 1
  minStack.pop()
  minStack.pop()
  minStack.push(3)
  minStack.push(4)
  minStack.push(2)
  print(minStack.getMin()) # return 2
  minStack.pop()
  print(minStack.top())    # return 2
  print(minStack.getMin()) # return 2
  minStack.pop()
  minStack.pop()
  minStack.push(5)
  minStack.push(6)
  print(minStack.getMin()) # return 5
  minStack.pop()
  print(minStack.top())    # return 6
  print(minStack.getMin()) # return 5
  minStack.pop()
  minStack.pop()
  
  minStack = MinStack1()
  minStack.push(1)
  minStack.push(2)
  minStack.push(0)
  print(minStack.getMin()) # return 0
  minStack.pop()
  print(minStack.top())    # return 2
  print(minStack.getMin()) # return 1
  minStack.pop()
  minStack.pop()
  minStack.push(3)
  minStack.push(4)
  minStack.push(2)
  print(minStack.getMin()) # return 2
  minStack.pop()
  print(minStack.top())    # return 2
  print(minStack.getMin()) # return 2
  minStack.pop()
  minStack.pop()
  minStack.push(5)
  minStack.push(6)
  print(minStack.getMin()) # return 5
  minStack.pop()
  print(minStack.top())    # return 6
  print(minStack.getMin()) # return 5
  minStack.pop()
  minStack.pop()
  
  minStack = MinStack2()
  minStack.push(1)
  minStack.push(2)
  minStack.push(0)
  print(minStack.getMin()) # return 0
  minStack.pop()
  print(minStack.top())    # return 2
  print(minStack.getMin()) # return 1
  minStack.pop()
  minStack.pop()
  minStack.push(3)
  minStack.push(4)
  minStack.push(2)
  print(minStack.getMin()) # return 2
  minStack.pop()
  print(minStack.top())    # return 2
  print(minStack.getMin()) # return 2
  minStack.pop()
  minStack.pop()
  minStack.push(5)
  minStack.push(6)
  print(minStack.getMin()) # return 5
  minStack.pop()
  print(minStack.top())    # return 6
  print(minStack.getMin()) # return 5
  minStack.pop()
  minStack.pop()
  