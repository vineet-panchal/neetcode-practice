# 287 - Find Duplicate Number
# Leetcode Link: https://leetcode.com/problems/find-the-duplicate-number/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

'''
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:
Input: nums = [1,2,3,2,2]
Output: 2

Example 2:
Input: nums = [1,2,3,4,4]
Output: 4

Constraints:
1 <= n <= 10000
nums.length == n + 1
1 <= nums[i] <= n
'''

# Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sorting algorithm
def findDuplicate(nums) -> int:
  nums.sort()
  for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:
      return nums[i]
  return -1



# HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)
def findDuplicate1(nums) -> int:
  seen = set()
  for num in nums:
    if num in seen:
      return num
    seen.add(num)
  return -1