# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        dummy = ListNode()
        cur = dummy
        r = 0

        while c1 and c2:
            a = (c1.val + c2.val + r) % 10
            b = ListNode(a)
            if (c1.val + c2.val) > 9:
                r = 1
            else:
                r = 0
            cur.next = b
            cur = cur.next
            c1 = c1.next
            c2 = c2.next
        
        while c1:
            a = (c1.val + r) % 10
            b = ListNode(a)
            if (c1.val + r) > 9:
                r = 1
            else:
                r = 0
            cur.next = b
            cur = cur.next
            c1 = c1.next

        while c2:
            a = (c2.val + r) % 10
            b = ListNode(a)
            if (c2.val + r) > 9:
                r = 1
            else:
                r = 0
            cur.next = b
            cur = cur.next
            c2 = c2.next
        
        if r == 1:
            b = ListNode(1)
            cur.next = b

        return dummy.next