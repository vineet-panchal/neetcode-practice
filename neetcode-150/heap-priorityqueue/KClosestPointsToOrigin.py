# 973 - K Closest Points to Origin
# Leetcode Link: https://leetcode.com/problems/k-closest-points-to-origin/

'''
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.
Return the k closest points to the origin (0, 0).
The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
You may return the answer in any order.

Example 1:
Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:
Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:
1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100
'''

# Solutions To The Problem:
import heapq

# Quick Select
# Time Complexity: O(n)
# Space Complexity: O(1)
def kClosest3(points, k):
  euclidean = lambda x: x[0] ** 2 + x[1] ** 2
  def partition(l, r):
    pivotIdx = r
    pivotDist = euclidean(points[pivotIdx])
    i = l
    for j in range(l, r):
      if euclidean(points[j]) <= pivotDist:
        points[i], points[j] = points[j], points[i]
        i += 1
    points[i], points[r] = points[r], points[i]
    return i

  L, R = 0, len(points) - 1
  pivot = len(points)

  while pivot != k:
    pivot = partition(L, R)
    if pivot < k:
      L = pivot + 1
    else:
      R = pivot - 1
  return points[:k]



# Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def kClosest2(points, k):
  points.sort(key=lambda p: p[0]**2 + p[1]**2)
  return points[:k]



# Max-Heap
# Time Complexity: O(n * log k)
# Space Complexity: O(k)
def kClosest1(points, k):
  maxHeap = []
  for x, y in points:
    dist = -(x ** 2 + y ** 2)
    heapq.heappush(maxHeap, [dist, x, y])
    if len(maxHeap) > k:
      heapq.heappop(maxHeap)

  res = []
  while maxHeap:
    dist, x, y = heapq.heappop(maxHeap)
    res.append([x, y])
  return res



# Min-Heap
# Time Complexity: O(k * log n)
# Space Complexity: O(n)
def kClosest(points, k):
  minHeap = []
  for x, y in points:
    dist = (x ** 2) + (y ** 2)
    minHeap.append([dist, x, y])

  heapq.heapify(minHeap)
  res = []
  while k > 0:
    dist, x, y = heapq.heappop(minHeap)
    res.append([x, y])
    k -= 1

  return res

if __name__ == "__main__":
  points = [[0, 2], [2, 2]]
  k = 1
  points1 = [[0, 2], [2, 0], [2, 2]]
  k1 = 2
  print("Test Case 1: points = ", points, " k = ", k)
  print("Expected Output: ", [[0, 2]])
  print("Test Case 2: points = ", points1, " k = ", k1)
  print("Expected Output: ", [[0, 2], [2, 0]], "\n")

  print("Min Heap -> Test Case 1: ", kClosest(points, k))
  print("Min Heap -> Test Case 2: ", kClosest(points1, k1), "\n")
  
  print("Max Heap -> Test Case 1: ", kClosest1(points, k))
  print("Max Heap -> Test Case 2: ", kClosest1(points1, k1), "\n")
  
  print("Sorting -> Test Case 1: ", kClosest2(points, k))
  print("Sorting -> Test Case 2: ", kClosest2(points1, k1), "\n")
  
  print("Quick Select -> Test Case 1: ", kClosest3(points, k))
  print("Quick Select -> Test Case 2: ", kClosest3(points1, k1), "\n")