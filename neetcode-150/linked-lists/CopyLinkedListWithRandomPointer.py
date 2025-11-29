# 138 - Copy List With Random Pointer
# Leetcode Link: https://leetcode.com/problems/copy-list-with-random-pointer/

'''
Initial Thoughts

Simplify the problem:
    - Given a linked list where each node has a random pointer
    - Create a deep copy of the list with correct next and random pointers
    - Return the head of the copied list

Pattern Recognition: Straightforward solution
    - Iterate through the list, create new nodes and copy values
    - Use a map to store original-to-copy node mapping
    - Set next and random pointers in a second pass
    - Simple but uses extra space

Pattern Recognition: Optimal solution
    - Interleave copied nodes with original nodes in one pass
    - Set random pointers using interleaved structure
    - Split lists to restore original and get copy
    - Achieve O(n) time and O(1) extra space
'''

# Definition for singly-linked list with a random pointer.
class Node(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution1:
    def copyRandomList(self, head: "Node") -> "Node":
        if head is None:
            return None
        cur = head
        while cur: # copy nodes
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = node.next

        cur = head
        while cur: # copy random pointers
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        ans = head.next
        cur = head
        while cur: # cut into 2 lists
            nxt = cur.next
            if nxt:
                cur.next = nxt.next
            cur = nxt
        return ans



class Solution: # with a map
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        node_map = {}

        # Create the copy nodes without next and random connections
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

        # Assign next and random connections for the copy nodes
        current = head
        while current:
            copy_node = node_map[current]
            copy_node.next = node_map.get(current.next)
            copy_node.random = node_map.get(current.random)
            current = current.next

        return node_map[head]

