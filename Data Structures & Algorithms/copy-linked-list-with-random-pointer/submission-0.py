"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        - I'm thinking a 2 pass alg
        - 1st pass, is us copying every value from the original list
            - create a new node with the same values and store in a dictionary oldNode:NewNode
        - 2nd pass, for each node in the old list, append the correct next and random
            - Create a 2 dummy node (1 to maintain head and the other for processing), and then for each node, process as you go
        - return second list
        '''
        if not head:
            return None
        start = head
        store = {}

        while start:
            newNode = Node(start.val)
            store[start] = newNode
            start = start.next

        start = head
        while start:
            curr = store[start]
            if start.random:
                curr.random = store[start.random]
            if start.next:
                curr.next = store[start.next]
            start = start.next

        return store[head]