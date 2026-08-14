# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = ListNode()
        dummy.next = res

        carry = 0
        while l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            print(f"s: {s}")
            res.val = s % 10
            carry = s // 10

            print(f"res.val: {res.val}")
            print(f"carry: {carry}")

            if l1 or l2:
                res.next = ListNode()
                res = res.next
        
        if carry > 0:
            res.next = ListNode(carry)
        
        return dummy.next

