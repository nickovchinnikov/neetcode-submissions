# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        has = set()

        while head:
            if head in has:
                return True
            else:
                has.add(head)
            head = head.next
        return False