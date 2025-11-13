'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:
Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
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
  


def reverseList1(head):
  if not head:
    return None
  
  newHead = head
  if head.next:
    newHead = reverseList1(head.next)
    head.next.next = head
  head.next = None
  
  return newHead


def reverseList(head):
  prev, curr = None, head

  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev

if __name__ == "__main__":
    head = build_list([0, 1, 2, 3])
    head2 = build_list([])
    reversed_head = reverseList(head)
    reversed_head2 = reverseList(head)
    print(to_list(reversed_head))  # [3, 2, 1, 0]
    print(to_list(reversed_head2)) # []
