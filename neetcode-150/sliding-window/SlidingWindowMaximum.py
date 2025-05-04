'''
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.
Return a list that contains the maximum element in the window at each step.

Example 1:
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]
Explanation: 
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
'''

# Brute Force Approach
def maxSlidingWindow(nums, k):
  output = []

  for i in range(len(nums) - k + 1):
    maxi = nums[i]
    for j in range(i, i + k):
      maxi = max(maxi, nums[j])
    output.append(maxi)

  return output
# Time complexity: O(n * k)
# Space complexity: O(n)



# Segment Tree Approach
class SegmentTree:
    def __init__(self, N, A):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.build(N, A)

    def build(self, N, A):
        self.tree = [float('-inf')] * (2 * self.n)
        for i in range(N):
            self.tree[self.n + i] = A[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def query(self, l, r):
        res = float('-inf')
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

def maxSlidingWindow1(nums, k):
  n = len(nums)
  segTree = SegmentTree(n, nums)
  output = []
  for i in range(n - k + 1):
    output.append(segTree.query(i, i + k - 1))
  return output
# Time complexity: O(n * log n)
# Space complexity: O(n)



# Heap Approach
def maxSlidingWindow2(nums, k):
  heap = []
  output = []
  for i in range(len(nums)):
    heap.heappush(heap, (-nums[i], i))
    if i >= k - 1:
      while heap[0][1] <= i - k:
        heap.heappop(heap)
      output.append(-heap[0][0])
  return output
# Time complexity: O(n * log k)
# Space complexity: O(k)



# Dynamic Programming Approach
def maxSlidingWindow3(nums, k):
  n = len(nums)
  leftMax = [0] * n
  rightMax = [0] * n

  leftMax[0] = nums[0]
  rightMax[n - 1] = nums[n - 1]

  for i in range(1, n):
    if i % k == 0:
      leftMax[i] = nums[i]
    else:
      leftMax[i] = max(leftMax[i - 1], nums[i])

    if (n - 1 - i) % k == 0:
      rightMax[n - 1 - i] = nums[n - 1 - i]
    else:
      rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - 1 - i])

    output = [0] * (n - k + 1)

  for i in range(n - k + 1):
    output[i] = max(leftMax[i + k - 1], rightMax[i])

  return output
# Time complexity: O(n)
# Space complexity: O(n)



# Deque Approach
from collections import deque
def maxSlidingWindow4(nums, k):
  output = []
  q = deque()  # index
  l = r = 0

  while r < len(nums):
    while q and nums[q[-1]] < nums[r]:
      q.pop()
    q.append(r)

    if l > q[0]:
      q.popleft()

    if (r + 1) >= k:
      output.append(nums[q[0]])
      l += 1
    r += 1

  return output
# Time complexity: O(n)
# Space complexity: O(k)
# Test cases
if __name__ == "__main__":
  # Test cases
  print(maxSlidingWindow([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]
  print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
  print(maxSlidingWindow([1], 1)) # [1]
  print(maxSlidingWindow([1,-1], 1)) # [1,-1]
  print(maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5)) # [10,9]
  print(maxSlidingWindow([4,-2], 2)) # [4]
  print(maxSlidingWindow([1,3,1,2,0,5], 3)) # [3,3,2,5]
  
  print(maxSlidingWindow1([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]
  print(maxSlidingWindow1([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
  print(maxSlidingWindow1([1], 1)) # [1]
  print(maxSlidingWindow1([1,-1], 1)) # [1,-1]
  print(maxSlidingWindow1([9,10,9,-7,-4,-8,2,-6], 5)) # [10,9]
  print(maxSlidingWindow1([4,-2], 2)) # [4]
  print(maxSlidingWindow1([1,3,1,2,0,5], 3)) # [3,3,2,5]
  
  print(maxSlidingWindow2([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]
  print(maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
  print(maxSlidingWindow2([1], 1)) # [1]
  print(maxSlidingWindow2([1,-1], 1)) # [1,-1] 
  print(maxSlidingWindow2([9,10,9,-7,-4,-8,2,-6], 5)) # [10,9]
  print(maxSlidingWindow2([4,-2], 2)) # [4]
  print(maxSlidingWindow2([1,3,1,2,0,5], 3)) # [3,3,2,5]
  
  print(maxSlidingWindow3([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]
  print(maxSlidingWindow3([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
  print(maxSlidingWindow3([1], 1)) # [1]
  print(maxSlidingWindow3([1,-1], 1)) # [1,-1]
  print(maxSlidingWindow3([9,10,9,-7,-4,-8,2,-6], 5)) # [10,9]
  print(maxSlidingWindow3([4,-2], 2)) # [4]
  print(maxSlidingWindow3([1,3,1,2,0,5], 3)) # [3,3,2,5]
  
  print(maxSlidingWindow4([1,2,1,0,4,2,6], 3)) # [2,2,4,4,6]
  print(maxSlidingWindow4([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
  print(maxSlidingWindow4([1], 1)) # [1]
  print(maxSlidingWindow4([1,-1], 1)) # [1,-1]
  print(maxSlidingWindow4([9,10,9,-7,-4,-8,2,-6], 5)) # [10,9]
  print(maxSlidingWindow4([4,-2], 2)) # [4]
  print(maxSlidingWindow4([1,3,1,2,0,5], 3)) # [3,3,2,5]