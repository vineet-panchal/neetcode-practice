'''
Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:
constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

Example 1:
Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
Output:
[null, 3, 3, 3, 5, 6]

Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   // return 3
kthLargest.add(5);   // return 3
kthLargest.add(6);   // return 3
kthLargest.add(7);   // return 5
kthLargest.add(8);   // return 6

Constraints:
1 <= k <= 1000
0 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= val <= 1000
There will always be at least k integers in the stream when you search for the kth integer.
'''

from typing import List
import heapq

# Sorting
# Time Complexity: O(m * n log n)
# Space Complexity: O(m)
class KthLargest1:
  def __init__(self, k: int, nums: List[int]):
    self.k = k
    self.arr = nums

  def add(self, val: int) -> int:
    self.arr.append(val)
    self.arr.sort()
    return self.arr[len(self.arr) - self.k]



# Min-Heap
# Time Complexity: O(m * log k)
# Space Complexity: O(k)
class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    self.minHeap = nums # set nums to be a min heap
    self.k = k 
    heapq.heapify(self.minHeap)
    while len(self.minHeap) > k:
        heapq.heappop(self.minHeap)
  
  def add(self, val: int) -> int:
    heapq.heappush(self.minHeap, val) # add the new value to the heap
    if len(self.minHeap) > self.k: 
      heapq.heappop(self.minHeap)
    return self.minHeap[0]

if __name__ == "__main__":
  print("Test Case 1: nums = ", [1, 2, 3, 3])
  print("Add 3, Expected Output: 3")
  print("Add 5, Expected Output: 3")
  print("Add 6, Expected Output: 3")
  print("Add 7, Expected Output: 5")
  print("Add 8, Expected Output: 6", "\n")
  
  kthLargest = KthLargest(3, [1, 2, 3, 3])
  print("Min-Heap, add 3, return: ", kthLargest.add(3))  # 3
  print("Min-Heap, add 5, return: ", kthLargest.add(5))  # 3
  print("Min-Heap, add 3, return: ", kthLargest.add(6))  # 3
  print("Min-Heap, add 5, return: ", kthLargest.add(7))  # 5
  print("Min-Heap, add 6, return: ", kthLargest.add(8), "\n")  # 6
  
  kthLargest1 = KthLargest1(3, [1, 2, 3, 3])
  print("Sorting, add 3, return: ", kthLargest1.add(3))  # 3
  print("Sorting, add 5, return: ", kthLargest1.add(5))  # 3
  print("Sorting, add 3, return: ", kthLargest1.add(6))  # 3
  print("Sorting, add 5, return: ", kthLargest1.add(7))  # 5
  print("Sorting, add 6, return: ", kthLargest1.add(8), "\n")  # 6