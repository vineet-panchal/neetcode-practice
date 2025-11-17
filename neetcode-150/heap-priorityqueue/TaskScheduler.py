# 621 - Task Scheduler
# Leetcode Link: https://leetcode.com/problems/task-scheduler/

'''
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
'''

# Solutions To The Problem:
from collections import Counter, deque
import heapq

# Brute Force
# Time Complexity: O(t * m)
# Space Complexity: O(t)
def leastInterval3(tasks, n):
  count = [0] * 26
  for task in tasks:
    count[ord(task) - ord('A')] += 1

  arr = []
  for i in range(26):
    if count[i] > 0:
        arr.append([count[i], i])

  time = 0
  processed = []
  while arr:
    maxi = -1
    for i in range(len(arr)):
      if all(processed[j] != arr[i][1] for j in range(max(0, time - n), time)):
        if maxi == -1 or arr[maxi][0] < arr[i][0]:
          maxi = i

    time += 1
    cur = -1
    if maxi != -1:
      cur = arr[maxi][1]
      arr[maxi][0] -= 1
      if arr[maxi][0] == 0:
        arr.pop(maxi)
    processed.append(cur)
  return time



# Math
# Time Complexity: O(m)
# Space Complexity: O(1)
def leastInterval2(tasks, n):
  count = [0] * 26
  for task in tasks:
    count[ord(task) - ord('A')] += 1

  maxf = max(count)
  maxCount = 0
  for i in count:
    maxCount += 1 if i == maxf else 0

  time = (maxf - 1) * (n + 1) + maxCount
  return max(len(tasks), time)



# Greedy
# Time Complexity: O(m)
# Space Complexity: O(1)
def leastInterval1(tasks, n):
  count = [0] * 26
  for task in tasks:
    count[ord(task) - ord('A')] += 1

  count.sort()
  maxf = count[25]
  idle = (maxf - 1) * n

  for i in range(24, -1, -1):
    idle -= min(maxf - 1, count[i])
  return max(0, idle) + len(tasks)



# Max-Heap
# Time Complexity: O(m)
# Space Complexity: O(1)
def leastInterval(tasks, n):
  count = Counter(tasks)
  maxHeap = [-cnt for cnt in count.values()]
  heapq.heapify(maxHeap)

  time = 0
  q = deque()  # pairs of [-cnt, idleTime]
  while maxHeap or q:
    time += 1

    if not maxHeap:
      time = q[0][1]
    else:
      cnt = 1 + heapq.heappop(maxHeap)
      if cnt:
        q.append([cnt, time + n])
    if q and q[0][1] == time:
      heapq.heappush(maxHeap, q.popleft()[0])
  return time

if __name__ == "__main__":
  tasks = ["X", "X", "Y", "Y"]
  n = 2
  tasks1 = ["A", "A", "A", "B", "C"]
  n1 = 3
  print("Test Case 1: tasks = ", tasks, " n = ", n)
  print("Expected Output: ", 5)
  print("Test Case 2: tasks = ", tasks1, " n = ", n1)
  print("Expected Output: ", 9, "\n")
  
  print("Max-Heap -> Test Case 1: ", leastInterval(tasks, n))
  print("Max-Heap -> Test Case 2: ", leastInterval(tasks1, n1), "\n")
  
  print("Greedy -> Test Case 1: ", leastInterval1(tasks, n))
  print("Greedy -> Test Case 2: ", leastInterval1(tasks1, n1), "\n")
  
  print("Math -> Test Case 1: ", leastInterval2(tasks, n))
  print("Math -> Test Case 2: ", leastInterval2(tasks1, n1), "\n")
  
  print("Brute Force -> Test Case 1: ", leastInterval3(tasks, n))
  print("Brute Force -> Test Case 2: ", leastInterval3(tasks1, n1), "\n")