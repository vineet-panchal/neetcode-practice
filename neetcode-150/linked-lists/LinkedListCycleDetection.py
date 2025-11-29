# 141 - Linked list Cycle
# Leetcode Link: https://leetcode.com/problems/linked-list-cycle/

'''
Initial Thoughts

Simplify the problem:
  - Given the head of a linked list, detect if there is a cycle
  - Return True if cycle exists, False otherwise
  - No index parameter, cycle is created by next pointer

Pattern Recognition: Straightforward solution
  - Use set to track visited nodes
  - If node is revisited, cycle exists
  - Simple but uses extra space

Pattern Recognition: Optimal solution
  - Use two pointers (slow/fast) to detect cycle
  - If pointers meet, cycle exists
  - Achieve O(n) time and O(1) space
  - Efficient for large lists
'''

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
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
Note: index is not given to you as a parameter.

Example 1:
Input: head = [1,2,3,4], index = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], index = -1
Output: false

Constraints:
1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
'''

# Solutions To The Problem
# Hash Set solution
# Time Complexity: O(n)
# Space Complexity: O(n)
def hasCycle(head):
  seen = set()
  cur = head
  while cur:
    if cur in seen:
      return True
    seen.add(cur)
    cur = cur.next
  return False


# Fast and Slow Pointers solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def hasCycle1(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False

if __name__ == "__main__":
  head1 = build_list([1, 2, 3, 4])
  cycle1 = hasCycle(head1)
  print(to_list(cycle1))
  head2 = build_list([1, 2])
  cycle2 = hasCycle(head2)
  print(to_list(cycle2))
  
  cycle3 = hasCycle1(head1)
  print(to_list(cycle3))
  cycle4 = hasCycle(head2)
  print(to_list(cycle4))