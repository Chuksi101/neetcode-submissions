# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stop = head
        start = dummy = ListNode()
        start.next = head
        
        while n > 0:
            stop = stop.next
            n -= 1
        
        while stop:
            start = start.next
            stop = stop.next

        start.next = start.next.next
        return dummy.next