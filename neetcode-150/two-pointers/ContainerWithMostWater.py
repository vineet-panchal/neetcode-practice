# 11 - Container With Most Water
# Leetcode Link: https://leetcode.com/problems/container-with-most-water/

'''
You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4
'''

# Nested Loops
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def maxArea(heights) -> int:
  result = 0
  for left in range(len(heights)):
    for right in range(left + 1, len(heights)):
      area = (right - left) * min(heights[left], heights[right])
      result = max(result, area)
  return result



# Two Pointers
# Time Complexity: O(log n)
# Space Complexity: O(1)
def maxArea1(heights) -> int:
  result = 0 # initialize result (the max area)
  left = 0 # set left pointer to the start of the list
  right = len(heights) - 1 # set right pointer to the end of the list

  while left < right: # while left is less than right
    area = (right - left) * min(heights[left], heights[right])
    # calculate the area of the current left element and right element
    # area = base (distance from left and right) * height (minimum between left pillar and right pillar)
    result = max(result, area) # set the result to be the max between previous max area and current max area

    if heights[left] < heights[right]: # if the left element is less than the right element
      left += 1 # then increment left pointer
    else: # else the right element is less than the left element
      right -= 1 # then decrement right pointer
  return result # return the resulting list

if __name__ == "__main__":
  heights = [1,7,2,5,4,7,3,6]
  print(maxArea(heights))
  print(maxArea1(heights))
  heights = [2,2,2]
  print(maxArea(heights))
  print(maxArea1(heights))