"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def dfs(n):
            if n in cloned:
                return cloned[n]

            newNode = Node(n.val)
            cloned[n] = newNode

            for i in n.neighbors:
                newNode.neighbors.append(dfs(i))
            
            return newNode

        return dfs(node) if node else None