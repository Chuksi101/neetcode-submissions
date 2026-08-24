# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None

        while head:
            # Assign rest of list to temp (Next Node)
            temp = head.next
            # Reverse the direction of the current node (current node points to the head of new list before becoming the head itself)
            head.next = dummy
            # Assign dummy to current head of new list (Moving dummy forward)
            dummy = head
            # Go to the next node in the original list
            head = temp
        
        return dummy