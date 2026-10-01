# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False

        temp = ListNode()
        dummy = ListNode()
        temp.next = dummy

        while l1 or l2:
            l1v = l2v = 0
            if l1:
                l1v = l1.val
            if l2:
                l2v = l2.val
            total = l1v + l2v
            if carry:
                total += 1
                carry = False
            if total > 9:
                carry = True
                total = total % 10
            t = ListNode(total)
            dummy.next = t
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            total = 0

        if carry:
            t = ListNode(1)
            dummy.next = t
            dummy = dummy.next

        return temp.next.next
            