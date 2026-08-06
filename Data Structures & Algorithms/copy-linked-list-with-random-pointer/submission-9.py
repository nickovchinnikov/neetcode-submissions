"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

def print_list(head):
    vals = []
    while head:
        vals.append((head.val, head.random))
        head = head.next
    print(vals) 

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Insert copies
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next

        # Add random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            # every 2 steps
            curr = curr.next.next

        # Separate the list
        curr = head
        copy_head = head.next

        while curr:
            copy = curr.next
            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next
            curr = curr.next

        return copy_head






