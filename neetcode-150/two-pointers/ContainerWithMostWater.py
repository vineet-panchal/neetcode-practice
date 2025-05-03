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

def maxArea(self, heights) -> int:
  result = 0
  for left in range(len(heights)):
    for right in range(left + 1, len(heights)):
      area = (right - left) * min(heights[left], heights[right])
      result = max(result, area)
  return result

def maxArea1(self, heights) -> int:
  result = 0
  left = 0
  right = len(heights) - 1

  while left < right:
    area = (right - left) * min(heights[left], heights[right])
    result = max(result, area)

    if heights[left] < heights[right]:
      left += 1
    else:
      right -= 1
  return result

if __name__ == "__main__":
  heights = [1,7,2,5,4,7,3,6]
  print(maxArea(heights))
  print(maxArea1(heights))
  heights = [2,2,2]
  print(maxArea(heights))
  print(maxArea1(heights))