# 84 - Largest Rectangle In Histogram
# Leetcode Link: 

'''
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7
Constraints:

1 <= heights.length <= 1000.
0 <= heights[i] <= 1000
'''

'''
Largest Rectangle in Histogram - Stack Solution
This is a classic problem that can be efficiently solved using a monotonic stack. The key insight is to find, for each bar, how far left and right it can extend while maintaining its height.
Approach
For each bar at position i with height h:

Find the nearest smaller bar on the left
Find the nearest smaller bar on the right
The rectangle with this bar as the minimum height extends between these boundaries
Area = height[i] × width

We use a monotonic increasing stack to efficiently find these boundaries in a single pass.
Algorithm

Maintain a stack of indices where heights are in increasing order
When we encounter a bar shorter than the stack top:

Pop from stack (this bar's right boundary is current position)
Calculate area using popped bar as minimum height
Left boundary is the new stack top (or -1 if stack is empty)


After processing all bars, pop remaining bars (their right boundary is the end)
'''

def largestRectangleArea(heights):
    """
    Find the largest rectangle area in a histogram.
    
    Time Complexity: O(n) - each bar is pushed and popped at most once
    Space Complexity: O(n) - for the stack
    """
    stack = []  # Stack stores indices of bars
    max_area = 0
    
    for i in range(len(heights)):
        # While current bar is shorter than stack top,
        # calculate area with stack top as smallest bar
        while stack and heights[i] < heights[stack[-1]]:
            height_index = stack.pop()
            height = heights[height_index]
            
            # Width: from bar after left boundary to current position
            # Left boundary is the new stack top (or -1 if empty)
            width = i if not stack else i - stack[-1] - 1
            
            max_area = max(max_area, height * width)
        
        stack.append(i)
    
    # Process remaining bars in stack
    # These bars extend to the end of the array
    while stack:
        height_index = stack.pop()
        height = heights[height_index]
        
        # Width extends to the end
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        
        max_area = max(max_area, height * width)
    
    return max_area


'''

How It Works - Example Walkthrough
For heights = [7,1,7,2,2,4]:

i=0, h=7: Stack = [0]
i=1, h=1: 1 < 7, so pop 0

Height = 7, Width = 1, Area = 7
Stack = [1]


i=2, h=7: Stack = [1, 2]
i=3, h=2: 2 < 7, so pop 2

Height = 7, Width = 1, Area = 7
Stack = [1, 3]


i=4, h=2: Stack = [1, 3, 4]
i=5, h=4: Stack = [1, 3, 4, 5]
Process remaining: Pop 5, 4, 3

When popping 4: Height = 2, Width = 4 (from position 2 to 5), Area = 8 ✓



Key Points

Monotonic Stack: Keeps indices in increasing order of heights
Width Calculation: right - left - 1 where left is the previous smaller element
Time Complexity: O(n) - each element pushed/popped once
Space Complexity: O(n) - for the stack

This is an optimal solution for the histogram problem!
'''