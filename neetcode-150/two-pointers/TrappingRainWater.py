'''
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
'''

'''
## Example Walkthrough

Let's trace `[0,2,0,3,1,0,1,3,2,1]`:
```
Initial:
left=0, right=9, leftMax=0, rightMax=1, result=0
         ↓                         ↓
height: [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
Iteration 1: leftMax(0) < rightMax(1) → process left

left=1, leftMax=max(0,2)=2, result += 2-2 = 0

Iteration 2: leftMax(2) > rightMax(1) → process right

right=8, rightMax=max(1,2)=2, result += 2-2 = 0

Iteration 3: leftMax(2) == rightMax(2) → process right

right=7, rightMax=max(2,3)=3, result += 3-3 = 0

Iteration 4: leftMax(2) < rightMax(3) → process left

left=2, leftMax=max(2,0)=2, result += 2-0 = 2 ✓

Iteration 5: leftMax(2) < rightMax(3) → process left

left=3, leftMax=max(2,3)=3, result += 3-3 = 2

Iteration 6: leftMax(3) == rightMax(3) → process right

right=6, rightMax=max(3,1)=3, result += 3-1 = 4 ✓

Iteration 7: leftMax(3) == rightMax(3) → process right

right=5, rightMax=max(3,0)=3, result += 3-0 = 7 ✓

Iteration 8: leftMax(3) == rightMax(3) → process right

right=4, rightMax=max(3,1)=3, result += 3-1 = 9 ✓

Now left=3, right=4, so left < right is false. Result = 9 ✓
'''

def trap(height) -> int:
  if not height: return 0 

  left = 0 # set left pointer to the start of the list
  right = len(height) - 1 # set right pointer to the end of the list
  leftMax = height[left] # track max height seen from the left
  rightMax = height[right] # track max height seen from the right 
  result = 0 # initialize result
    
  while left < right: # while left is less than right
    if leftMax < rightMax: 
    # We know leftMax is the limiting factor
    # Safe to calculate water at left position
    # if left max is less than right max:
    # there's a wall at least right max somewhere to the right
    # So water at position left will be trapped up to leftMax level
    # Water trapped = leftMax - height[left]
      left += 1 # increment left pointer
      leftMax = max(leftMax, height[left]) # calculate left max
      result += leftMax - height[left] # increment result with the water trapped
    else:
    # rightMax <= leftMax, so rightMax is the limiting factor
    # Safe to calculate water at right position
      right -= 1 # decrement right index
      rightMax = max(rightMax, height[right]) # calculate the right max
      result += rightMax - height[right] # increment result with the water trapped
  return result # return the resulting water trapped