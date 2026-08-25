# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        For all n > 2:
            Go to the middle of the list
            reverse from the middle to the end (//2)
            Use the first from each one starting with the original head
        '''
        if head.next is None or head.next.next is None:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode
        second = prev

        while head and second:
            first_next = head.next
            second_next = second.next

            head.next = second
            second.next = first_next

            head = first_next
            second = second_next
        
