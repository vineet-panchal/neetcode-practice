# 1046 - Last Stone Weight
# Leetcode Link: https://leetcode.com/problems/last-stone-weight/

'''
You are given an array of integers stones where stones[i] represents the weight of the ith stone.
We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:
Input: stones = [2,3,6,2,4]
Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:
Input: stones = [1,2]
Output: 1

Constraints:
1 <= stones.length <= 20
1 <= stones[i] <= 100
'''

# Solutions To The Problem:
import heapq

# Bucket Sort
# Time Complexity: O(n + w)
# Space Complexity: O(w)
def lastStoneWeight3(stones) -> int:
  maxStone = max(stones)
  bucket = [0] * (maxStone + 1)
  for stone in stones:
    bucket[stone] += 1

  first = second = maxStone
  while first > 0:
    if bucket[first] % 2 == 0:
      first -= 1
      continue

    j = min(first - 1, second)
    while j > 0 and bucket[j] == 0:
      j -= 1

    if j == 0:
      return first
    second = j
    bucket[first] -= 1
    bucket[second] -= 1
    bucket[first - second] += 1
    first = max(first - second, second)
  return first



# Binary Search
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def lastStoneWeight2(stones) -> int:
  stones.sort()
  n = len(stones)

  while n > 1:
    cur = stones.pop() - stones.pop()
    n -= 2
    if cur > 0:
      l, r = 0, n
      while l < r:
        mid = (l + r) // 2
        if stones[mid] < cur:
          l = mid + 1
        else:
          r = mid
      pos = l
      n += 1
      stones.append(0)
      for i in range(n - 1, pos, -1):
        stones[i] = stones[i - 1]
      stones[pos] = cur
  return stones[0] if n > 0 else 0



# Sorting
# Time Complexity: O(n^2 log n)
# Space Complexity: O(n)
def lastStoneWeight1(stones) -> int:

  while len(stones) > 1:
    stones.sort()
    cur = stones.pop() - stones.pop()
    if cur:
      stones.append(cur)

  return stones[0] if stones else 0



# Heap
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def lastStoneWeight(stones) -> int:
  stones = [-s for s in stones]
  heapq.heapify(stones)

  while len(stones) > 1:
    first = heapq.heappop(stones)
    second = heapq.heappop(stones)
    if first != second:
      heapq.heappush(stones, first - second)

  stones.append(0)
  return abs(stones[0])

if __name__ == "__main__":
  stones = [2, 3, 6, 2, 4]
  stones1 = [1, 2]
  print("Test Case 1: ", stones)
  print("Expected Output: ", 1)
  print("Test Case 2: ", stones1)
  print("Expected Output: ", 1, "\n")
  
  print("Heap -> Test Case 1: ", lastStoneWeight(stones))
  print("Heap -> Test Case 2: ", lastStoneWeight(stones1), "\n")
  
  print("Sorting -> Test Case 1: ", lastStoneWeight(stones))
  print("Sorting -> Test Case 2: ", lastStoneWeight(stones1), "\n")
  
  print("Binary Search -> Test Case 1: ", lastStoneWeight(stones))
  print("Binary Search -> Test Case 2: ", lastStoneWeight(stones1), "\n")
  
  print("Bucket Sort -> Test Case 1: ", lastStoneWeight(stones))
  print("Bucket Sort -> Test Case 2: ", lastStoneWeight(stones1), "\n")